# PQComb-Codes Documentation

Source code for the paper [*Parameterized quantum comb and simpler circuits for reversing unknown qubit-unitary operations*](https://arxiv.org/abs/2403.03761).

PQComb is a novel quantum framework that employs parameterized quantum circuits to transform quantum processes. This approach simplifies complex quantum operations by treating them as trainable network components, similar to neural networks in classical machine learning. By optimizing these quantum components through iterative training, PQComb would be an efficient tool for quantum algorithmic design.

The table below outlines the Python files used to reproduce data for the visualizations and protocols in the PQComb paper. Related visual codes and original data are available from the corresponding authors upon reasonable request.

| Visualization / Protocols in the paper      | Location in this repository                                           | Extra hardware requirement |
|--------------------|------------------------------------------------------------------|:-----------------:|
| [Table I](./unitary_inversion/d%20=%202/comb_inversion.ipynb)      | `unitary_inversion/d = 2/comb_inversion.ipynb`                              | \ |
| [Figure 2](./unitary_inversion/d%20=%202/4-call%20protocol%20in%20Theorem%201.ipynb)           | `unitary_inversion/d = 2/4-call protocol in Theorem 1.ipynb`                              | \ |
| [Figure S4b](./unitary_inversion/d%20=%202/5-call%20protocol%20in%20Corollary%202.ipynb)             | `unitary_inversion/d = 2/5-call protocol in Corollary 2.ipynb` | \ |
| [Figure S5 (a-d)](./unitary_inversion/d%20=%202/Derivation%20of%20the%20training%20ansatz%20(a-d).ipynb)             | `unitary_inversion/d = 2/Derivation of the training ansatz (a-d).ipynb` | \ |
| [Figure S5 (e)](./unitary_inversion/d%20=%202/Derivation%20of%20the%20training%20ansatz%20(e).ipynb)             | `unitary_inversion/d = 2/Derivation of the training ansatz (e).ipynb` | \ |
| [Figure 3](./unitary_inversion/d%20=%202/noise%20simulation)              | `unitary_inversion/d = 2/noise simulation`      | Access to IBMQ devices |
| [Table II (a)](./unitary_inversion/d%20=%203/swap_inversion.ipynb)       | `unitary_inversion/d = 3/swap_inversion.ipynb`      | GPU |
| [optimal protocol in Table II (a)](./unitary_inversion/d%20=%203/10-slots%20protocol.ipynb)       | `unitary_inversion/d = 3/10-slots protocol.ipynb`      | \ |
| [Table II (b)](./unitary_transpose/swap_transpose.ipynb)       | `unitary_transpose/swap_transpose.ipynb`      | GPU |
| [optimal protocol in Table II (b)](./unitary_transpose/7-slots%20protocol.ipynb)       | `unitary_transpose/7-slots protocol.ipynb`      | \ |
| [channel discrimination protocol](./channel_discrimination/channel%20protocol.ipynb)       | `channel_discrimination/channel protocol.ipynb`      | \ |

## Repository Structure

```plaintext
PQCOMB-CODES/
├── unitary_inversion/                    # Unitary inversion
│   ├── d = 2                             # qubit-unitary inversion
│   │   ├── noise simulation/             # noise simulation for inversion
│   ├── d = 3                             # qutrit-unitary inversion
├── unitary_transpose/                    # qutrit-unitary transpose
└── channel_discrimination/               # Quantum channel discrimination task
```

## How to Run These Files?

We recommend running these files by creating a virtual environment using `conda` and install Jupyter Notebook. We recommend using Python `3.10` for compatibility.

```bash
conda create -n pqcomb python=3.10
conda activate pqcomb
conda install jupyter notebook
```

These codes are highly dependent on the [QuAIRKit](https://github.com/QuAIR/QuAIRKit) package no lower than v0.3.0. This package is featured for batch and qudit computations in quantum information science and quantum machine learning. The minimum Python version required for QuAIRKit is `3.8`.

To install QuAIRKit, run the following commands:

```bash
pip install quairkit
```

## System and Package Versions

It is recommended to run these files on a High Performance Computing (HPC) system, especially for tasks involving large datasets or complex simulations. Below are our Python package versions:

**Package Versions**:

- quairkit: 0.3.0
- torch: 2.4.1+cu121
- torch cuda: 12.1
- numpy: 1.26.4
- scipy: 1.14.1
- matplotlib: 3.9.2

**System Information**:

- Python version: 3.10.14
- OS: Linux, Ubuntu (version: #123-Ubuntu SMP Mon Jun 10 08:16:17 UTC 2024)
- CPU: Intel(R) Xeon(R) Platinum 8378A CPU @ 3.00GHz
- GPU: NVIDIA A800 80GB PCIe (6 GPUs in total)

These settings ensure compatibility and optimal performance when running the PQComb codes.
