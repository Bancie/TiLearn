---
title: Introduction to TiLearn
description: This document provides an overview of project content and the generalization of the various problems it addresses
hide:
  - navigation
---
# Introduction to TiLearn

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

**TiLearn** is an innovative open-source project dedicated to optimizing time management and providing advanced scheduling solutions through AI. This platform is grounded in the principles of Operations Research, a critical field focused on the efficient allocation of resources and the optimization of processes. By harnessing these techniques, TiLearn empowers individuals and teams to streamline their daily routines, enhance productivity, and achieve their goals more effectively.

At its core, TiLearn integrates the latest advancements in artificial intelligence with well-established scheduling methods to provide customized solutions. From minimizing task completion times to reducing delays, our project delivers innovative approaches that adapt to your unique requirements. Join us in shaping a future where efficient time management is accessible to everyone, helping you stay on track.

## List of Symbols and Their Meanings

- **\(\alpha \: | \: \beta \: | \: \gamma\)**: Notation used to identify the type of problem. Here, \(\alpha\) represents the number of machines that need scheduling. For the **single machine** case, it is denoted as \(\alpha = 1\), i.e., \(1|\beta|\gamma\). The \(\beta\) field specifies any constraints of the problem, while \(\gamma\) denotes the objective to be optimized.

| SYMBOLS | MEANING |
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

## References

[1] Le Minh Huy. *Single Machine Scheduling*.

[2] Michael Pinedo. *Scheduling: Theory, Algorithms, And Systems*. 01 2008.

[3] M.L. Pinedo. *Planning and Scheduling in Manufacturing and Services*. Springer series in operations research. Springer New York, 2009.

[4] PMI, editor. *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Project Management Institute, Newtown Square, PA, 5th edition, 2013.

[5] Krzysztof Postek, Alessandro Zocca, Joaquim Gromicho, and Jeffrey Kantor. *Hands-On Mathematical Optimization with AMPL in Python*. Online, 2024.