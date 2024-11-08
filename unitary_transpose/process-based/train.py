import gc
import time
from typing import List, Tuple

import numpy as np
import quairkit as qkit
import torch
from quairkit import Circuit, State, to_state
from quairkit.database import *
from quairkit.qinfo import *


def create_circuit(data: torch.Tensor, system_dim: List[int], L: int) -> Circuit:
    circuit = Circuit(len(system_dim), system_dim=system_dim)

    for _ in range(L):
        circuit.universal_qudits([0, 1])
        
        circuit.oracle(data, system_idx=[1], latex_name=r'$U$')

    circuit.universal_qudits([0, 1])
    return circuit


def predict(size: int, param: torch.Tensor, system_dim: List[int], L: int) -> float:
    test_state = bell_state(2, 3)
    input_state = to_state(torch.kron(zero_state(1, system_dim[:-2]).ket, 
                                      test_state.ket),
                           system_dim=system_dim)
    
    test_batch = random_unitary(1, size=size, system_dim=3)
    new_cir = create_circuit(test_batch, system_dim, L)
    new_cir.update_param(param)
    
    new_cir.oracle(test_batch.conj(), system_idx=[1], latex_name=r'$U^*$')
    
    output_state = new_cir(input_state)
    output_state = output_state.trace(0)
    return torch.mean((test_state.bra @ output_state.density_matrix @ test_state.ket).real).item()


def train(data_set: torch.Tensor, dim_ancilla: int, L: int, NUM_ITR: int, LR: float) -> Tuple[float, Circuit]:
    r"""Train the target unitary transformation.
    
    Args:
        data: input data of unitary transformation.
        dim_ancilla: Dimension of the ancilla.
        L: Number of layers.
        NUM_ITR: Number of iterations.
        LR: Learning rate.
    
    Note:
        below implementation is just .py output of the jupyter notebook.
    
    """
    size, dim_unitary = len(data_set), data_set.shape[-1]
    train_set = data_set
    
    expec_state = bell_state(2, dim_unitary)
    expec_state._evolve(train_set.transpose(-1, -2), [0])
    
    system_dim = [dim_ancilla, dim_unitary, dim_unitary]
    cir = create_circuit(train_set, system_dim, L)
    
    input_state = to_state(torch.kron(zero_state(1, system_dim[:-2]).ket, 
                                      bell_state(2, system_dim[-2:]).ket),
                           system_dim=system_dim)

    def loss_fcn(circuit: Circuit) -> torch.Tensor:
        output_state = circuit(input_state)
        
        output_state = output_state.trace(0)
        return 1 - torch.mean((expec_state.bra @ output_state.density_matrix @ expec_state.ket).real)
    
    loss_list, time_list, str_list = [], [], []
    opt = torch.optim.Adam(lr=LR, params=cir.parameters()) # cir is a Circuit type
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(opt, 'min', factor=0.5) # activate scheduler

    for itr in range(NUM_ITR):
        start_time = time.time()
        opt.zero_grad()
        loss = loss_fcn(cir) # compute loss

        loss.backward()
        opt.step()
        scheduler.step(loss) # activate scheduler

        loss = loss.item()
        loss_list.append(loss)
        time_list.append(time.time() - start_time)

        if itr % (NUM_ITR // 20) == 0 or itr == NUM_ITR - 1:
            fidelity, last_lr = 1 - loss, scheduler.get_last_lr()[0]
            
            
            print_str = f"    iter: {itr}, train fidelity: {fidelity:.8f}, "
            print_str += f"lr: {last_lr:.2E}, avg_time: {np.mean(time_list):.4f}s"
            print(print_str)
            
            time_list = []
            str_list.append(print_str + "\n")
            
            if last_lr < 1e-6:
                break
    
    param = cir.param.clone()
    del cir
    gc.collect()
    torch.cuda.empty_cache()
    fidelity = np.stack([predict(size * 2, param, system_dim, L) for _ in range(5)]).mean()
    return fidelity, str_list


if __name__ == '__main__':
    import itertools
    qkit.set_dtype('complex128')
    qkit.set_device('cuda:5')
    
    dim_unitary = 3
    NUM_ITR, LR = 40000, 0.2
    train_size = 10000
    
    data_set = random_unitary(1, size=train_size, system_dim=dim_unitary)
    list_L = [1, 2, 3, 4, 5, 6, 7]
    list_dim_ancilla = [3, 6, 9, 12, 18, 24, 27]
    
    list_L.reverse()
    list_dim_ancilla.reverse()
    assert min(list_dim_ancilla) >= 2

    for L, dim_ancilla in itertools.product(list_L, list_dim_ancilla):
        print(f"\nTraining with L={L}, dim_ancilla={dim_ancilla}")
        fidelity, str_list = train(data_set, dim_ancilla, L, NUM_ITR, LR)
        
        overall_message = f"Number of slots = {L}, Ancilla dimension = {dim_ancilla}, Test Fidelity = {fidelity}\n"
        with open("training_summary.txt", "a") as file:
            file.write(overall_message)
        with open("training_log.txt", "a") as file:
            file.write(overall_message)
            for message in str_list:
                file.write(message)
