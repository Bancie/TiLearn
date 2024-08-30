---
title: Introduction to TiLearn
description: This document provides an overview of project content and the generalization of the various problems it addresses
hide:
  - navigation
---
# TiLearn: Getting Started

<a href="https://web.facebook.com/ngchibangg?__cft__[0]=AZUZx_Pe8u4-tiSh77gJQ1HR1YJ7SNb7CqCvr0Hkf8oO69J2fwebFyWGl9r68Kg3WmgWsUa-RCwdT2HzRTdCC8WW45Gtx_wO4AjBJKgfcLuIG94XDOYjlqq7SbS4q4D-KTjM8_CR_GQ5ZkeG7cliEFmlX6VyeDFxH5Jo8ubWPIg60g&__tn__=-]C%2CP-R" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Bancie/Optimization-Oracle/assets/144613141/e36031e2-c050-4f56-8c53-c4d851772af3" style="max-width: 100%; width: 400px; margin-bottom: 20px">
    <img alt="Bancie logo" src="https://github.com/Bancie/TiLearn/assets/144613141/ceb3dfd0-a358-4a46-b478-0a5235496cc7" width="400px">
  </picture>
</a>
<a href="https://web.facebook.com/ngchibangg?__cft__[0]=AZUZx_Pe8u4-tiSh77gJQ1HR1YJ7SNb7CqCvr0Hkf8oO69J2fwebFyWGl9r68Kg3WmgWsUa-RCwdT2HzRTdCC8WW45Gtx_wO4AjBJKgfcLuIG94XDOYjlqq7SbS4q4D-KTjM8_CR_GQ5ZkeG7cliEFmlX6VyeDFxH5Jo8ubWPIg60g&__tn__=-]C%2CP-R" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Bancie/Optimization-Oracle/assets/144613141/e36031e2-c050-4f56-8c53-c4d851772af3" style="max-width: 100%; width: 400px; margin-bottom: 20px">
    <img alt="Bancie logo" src="https://github.com/Bancie/TiLearn/assets/144613141/9c35f828-8c29-444e-aafb-f298c2bdba93" width="400px">
  </picture>
</a>
<h3></h3>

## Introduction

**TiLearn** is a Python package designed to optimize time management and provide advanced scheduling solutions using AI. This platform is grounded in the principles of Operations Research, a critical field focused on the efficient allocation of resources and the optimization of processes. By harnessing these techniques, TiLearn empowers individuals and teams to streamline their daily routines, enhance productivity, and achieve their goals more effectively.

At its core, TiLearn integrates the latest advancements in artificial intelligence with well-established scheduling methods to provide customized solutions. From minimizing task completion times to reducing delays, our project delivers innovative approaches that adapt to your unique requirements. Join us in shaping a future where efficient time management is accessible to everyone, helping you stay on track.

## How to Install

Before installing **TiLearn**, ensure you have the following:

- **Python**: Make sure you have Python 3.10.0 or higher installed. You can check your Python version by running the following command in your terminal:

    ```bash
    python --version
    ```

    or 

    ```bash
    python3 --version
    ```

- **pip**: The Python package installer, `pip`, should be installed. You can verify if `pip` is installed by running:

    ```bash
    pip --version
    ```

    If `pip` is not installed, you can install it by following the instructions [here](https://pip.pypa.io/en/stable/installation/).

### Installation

Once you have the prerequisites, you can install **TiLearn** using pip. To install the latest version of **TiLearn**, run the following command:

```bash
pip install TiLearn
```

After the installation is complete, you can verify that **TiLearn** has been installed successfully by running:

```bash
pip show TiLearn
```

This command will display the package information, including the version number and installation path.

### Use It

After successfully installing **TiLearn**, you can begin using it in your Python scripts by importing it as follows

```python
import tilearn
```

## Understanding
### List of Symbols and Their Meanings

**\(\alpha \: | \: \beta \: | \: \gamma\)**: Notation used to identify the type of problem. Here, \(\alpha\) represents the number of machines that need scheduling. For the **single machine** case, it is denoted as \(\alpha = 1\), i.e., \(1 \: | \: \beta \: | \: \gamma\). The \(\beta\) field specifies any constraints of the problem, while \(\gamma\) denotes the objective to be optimized.

The details of the other element symbols are shown in the table below:

| Symbol | Description |
| :------: | ------ | 
| **\(J_{ij}\)** | The \(j\)-th **job** processed on the \(i\)-th machine; in the single machine case, this is simply denoted as \(J_j\). |
| **\(p_j\)** | **Processing time** of the \(j\)-th job, which is the time from the start to the completion of the job. |
| **\(d_j\)** | **Due date** of the \(j\)-th job. |
| **\(C_j\)** | **Completion time** of the \(j\)-th job. |
| **\(C_{\max}\)** | The **maximum completion time (makespan)** of all jobs, calculated as \(C_{\max} = \underset{1 \leq j \leq n}{\max} C_j\). |
| **\(S_j\)** | **Starting time** of the \(j\)-th job, defined as \(S_j = \max (C_{j-1}, r_j)\). |
| **\(r_j\)** | **Release time** of the \(j\)-th job. If \(r_j \neq 0\), the job cannot start before time \(r_j\) (\(S_j \geq r_j\)). If \(r_j = 0\), the job can start at any time. |
| **\(W_j\)** | **Waiting time** of the \(j\)-th job, which is the time from when the job is ready to when it starts, defined as \(W_j = S_j - r_j = C_j - p_j - r_j\). |
| **\(F_j\)** | **Flow time** of the \(j\)-th job, which is the time from when the job is ready to when it completes, defined as \(F_j = C_j - r_j = W_j + p_j\). |
| \(w_j\)     | The weight of job \(j\), i.e., the priority level assigned to job \(j\). |
| \(L_j\)     | The lateness of job \(j\), defined as the amount of time from \(d_j\) to \(C_j\), calculated by the formula \(L_j = C_j - d_j\). If \(L_j < 0\), the job is completed earlier than its deadline, while if \(L_j > 0\), the job is completed later than its deadline. |
| \(T_j\)     | The tardiness of job \(j\), which is a measure of how late job \(j\) is defined through \(L_j\). If \(L_j \leq 0\), then \(T_j = 0\); otherwise, if \(L_j > 0\), \(T_j = L_j\), or \(T_j = \max(L_j, 0)\). |
| \(E_j\)     | The earliness of job \(j\), which is a measure of how early job \(j\) is defined through \(L_j\). If \(L_j \geq 0\), then \(E_j = 0\); otherwise, if \(L_j < 0\), \(E_j = L_j\), or \(E_j = \max(\mid L_j \mid, 0)\). |
| \(prec\)    | A problem with precedence constraints. If \(prec\) appears in the problem class \(\beta\), it means that some jobs must be completed before other jobs can start, also known as predecessor and successor jobs. If each job in the problem has at most one predecessor and one successor, the problem forms a chain. If each job has at most one successor, the problem forms an in-tree. Conversely, if each job has at most one predecessor, the problem forms an out-tree. If \(prec\) does not appear in the problem class \(\beta\), the jobs can be scheduled freely. |
| \(prmp\)    | A problem with preemption, usually used when \(r_j \neq 0\). If \(prmp\) appears in the problem class \(\beta\), it means that jobs can be interrupted at any point and resumed later to achieve the objective of the problem. Conversely, if \(prmp\) does not appear in the problem class \(\beta\), jobs cannot be interrupted. |

### Scheduling Problem Types

This Python package solves different types of scheduling problems commonly encountered in operations research and optimization.

Each problem type focuses on various objectives, such as minimizing the maximum lateness of jobs or the total weighted completion time. The problems are categorized based on job constraints, such as independence, precedence requirements, and release times, providing a comprehensive framework for effectively managing and optimizing job schedules.

For **single machine scheduling**, we have a list of types shown below:

- The Maximum Lateness $\big(L_{\max}\big)$
    - Independence jobs $\big(1 \: | \:  \: | \: L_{\max}\big)$
    - Release jobs $\big(1 \: | \: r_j \: | \: L_{\max}\big)$
- The Total (Weighted) Completion Time $\big(\sum w_j C_j\big)$
    - Independence jobs $\big(1 \: | \:  \: | \: \sum w_j C_j\big)$
    - Sequence jobs $\big(1 \: | \: prec \: | \: \sum w_j C_j\big)$
    - Release jobs $\big(1 \: | \: r_j \: | \: \sum w_j C_j\big)$


For a more in-depth understanding of how each type of scheduling problem works, check out the [user guide](../user-guide/index.md).

## References

[1] Le Minh Huy. *Single Machine Scheduling*.

[2] Michael Pinedo. *Scheduling: Theory, Algorithms, And Systems*. 01 2008.

[3] M.L. Pinedo. *Planning and Scheduling in Manufacturing and Services*. Springer series in operations research. Springer New York, 2009.

[4] PMI, editor. *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Project Management Institute, Newtown Square, PA, 5th edition, 2013.

[5] Krzysztof Postek, Alessandro Zocca, Joaquim Gromicho, and Jeffrey Kantor. *Hands-On Mathematical Optimization with AMPL in Python*. Online, 2024.