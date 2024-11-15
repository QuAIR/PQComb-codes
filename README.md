# PQComb-Codes Documentation

Source code for the paper [*Parameterized quantum comb and simpler circuits for reversing unknown qubit-unitary operations*](https://arxiv.org/abs/2403.03761).

PQComb is a novel quantum framework that employs parameterized quantum circuits to transform quantum processes. This approach simplifies complex quantum operations by treating them as trainable network components, similar to neural networks in classical machine learning. By optimizing these quantum components through iterative training, PQComb would be an efficient tool for quantum algorithmic design.

The table below outlines the Python files used to reproduce data for the figures and tables in the PQComb paper. Related visualization codes and original data are available from the corresponding authors upon reasonable request.

| Data in the paper      | Location in this repository                                           |
|--------------------|------------------------------------------------------------------|
| [Table I](./unitary_inversion/d%20=%202/4-call%20protocol%20in%20Theorem%201.ipynb)      | `unitary_inversion/d = 2/comb-based`                              |
| [Figure 2](./unitary_inversion/d%20=%202/comb-based/comb_inversion.ipynb)           | `unitary_inversion/d = 2/4-call protocol in Theorem 1.ipynb`                              |
| [Figure 3](./unitary_inversion/d%20=%202/noise%20simulation)              | `unitary_inversion/d = 2/noise simulation`      |
| Table II (a)       | `unitary_inversion/d = 3`      |
| Table II (b)       | `unitary_transpose`      |
| [Figure S4b](./unitary_inversion/d%20=%202/5-call%20protocol%20in%20Corollary%202.ipynb)             | `unitary_inversion/d = 2/5-call protocol in Corollary 2.ipynb` |
| [Figure S5](./unitary_inversion/d%20=%202/Derivation%20of%20the%20training%20ansatz.ipynb)             | `unitary_inversion/d = 2/Derivation of the training ansatz.ipynb` |

## Repository Structure

```plaintext
PQCOMB-CODES/
├── channel_discrimination/               # Quantum channel discrimination methods.
├── unitary_inversion/                    # Unitary inversion techniques.
│   ├── d = 2                             # Implementations for dimension d=2.
│   │   ├── comb-based/                   # Comb-based approach for inversion.
│   │   ├── noise simulation/             # Noise simulation for inversion.
│   │   ├── process-based/                # Process-based inversion methods.
│   │   ├── refinement/                   # Refinement techniques for inversion.
│   │   └── swap/                         # Swap-based inversion approach.
│   ├── d = 3                             # Implementations for dimension d=3.
│   │   ├── comb-based/                   # Comb-based approach for inversion.
│   │   ├── process-based/                # Process-based inversion methods.
│   │   └── swap/                         # Swap-based inversion approach.
└── unitary_transpose/                    # Unitary transpose calculations.
    ├── process-based/                    # Process-based transpose methods.
    └── swap/                             # Swap-based transpose methods.
```


## How to Install QuAIRKit

The minimum Python version required for QuAIRKit is `3.8`. We recommend using Python `3.10` for compatibility.

To create a virtual environment using `conda` and install Jupyter Notebook:

```bash
conda create -n quair python=3.10
conda activate quair
conda install jupyter notebook
```

To install QuAIRKit using `pip`:

```bash
pip install quairkit
```

Alternatively, clone the repository and install it locally:

```bash
git clone https://github.com/QuAIR/QuAIRKit
cd QuAIRKit
pip install -e .
```

For the latest information, please visit [QuAIRKit on GitHub](https://github.com/QuAIR/QuAIRKit).


## System and Package Versions

It is recommended to run this project on a High Performance Computing (HPC) system, especially for tasks involving large datasets or complex simulations. Below are the tested versions of required packages and system specifications:

**Package Versions**:
- quairkit: 0.2.0
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
