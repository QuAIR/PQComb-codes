# PQComb-Codes Documentation

Source code for the PQComb paper [arXiv:2403.03761](https://arxiv.org/abs/2403.03761).

## Full Description

This repository provides the source code for reproducing the results presented in the PQComb paper, focusing on the practical implementation of quantum process quantization using methods such as quantum channel discrimination, unitary inversion, and unitary transpose. These techniques are foundational for tasks in quantum computing, such as state estimation, process characterization, and error correction.

The repository is divided into separate components, each exploring different approaches (e.g., comb-based, process-based) across various quantum dimensions (`d`). The main objective is to provide a versatile toolkit for understanding and utilizing these methods effectively in research and practical quantum computing scenarios.

The core areas of this repository include:

- **Unitary Inversion**: Methods to calculate the inverse of unitary processes, which is crucial for quantum process control.
- **Unitary Transpose**: Techniques to compute the transpose of unitary matrices, aiding in state transformations and machine learning applications.
- **Channel Discrimination**: Quantum algorithms for distinguishing between different quantum channels.

## Overall Structure

```
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

### Main Modules Overview

1. **Channel Discrimination**:
   - Implements algorithms to distinguish between quantum channels, which is critical for error correction and channel coding. The `channel_discrimination.ipynb` notebook demonstrates multiple methods for channel discrimination, showcasing their effectiveness and applications.

2. **Unitary Inversion**:
   - Techniques to compute the inverse of unitary operators. This is key in many quantum algorithms where inversion is required for optimization or control.
   - The `comb_inversion.ipynb`, `process_inversion.ipynb`, and `swap_inversion.ipynb` notebooks provide methods for inversion, with examples and analysis to understand their performance. The **noise simulation** section highlights the challenges associated with noise and how it affects inversion feasibility.

3. **Unitary Transpose**:
   - Methods to calculate the transpose of unitary matrices, useful in machine learning and state transformation tasks.
   - `process_transpose.ipynb` and `swap_transpose.ipynb` provide practical guides for these techniques, emphasizing complexity, use cases, and detailed examples.
## Visualization Data Reference

The following table provides an overview of where to locate the data visualizations corresponding to the figures and tables presented in the PQComb paper:

| Visualization      | Location in Repository                                           |
|--------------------|------------------------------------------------------------------|
| Table I (d=2)      | `unitary_inversion/d = 2/comb-based`                              |
|                    | `unitary_inversion/d = 2/process-based`                          |
|                    | `unitary_inversion/d = 2/swap`                                    |
| Fig 3              | `unitary_inversion/d = 2/noise simulation`                        |
| Fig S3             | `unitary_inversion/d = 2/refinement`                              |
| Table I (d=3)      | `unitary_inversion/d = 3/comb-based`                              |
|                    | `unitary_inversion/d = 3/process-based`                          |
| Table II           | `unitary_inversion/d = 3/swap`                                    |
| Table III          | `unitary_transpose/process-based`                                 |
| Table IV           | `unitary_transpose/swap`                                          |

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

