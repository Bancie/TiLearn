---
title: User Guide
description: This document categorizes all the problems, detailing their foundational concepts, relevant materials, and solutions
---
# User Guide Overview

When dealing with **single machine scheduling**, there are various types of scheduling problems to consider.

The list of these types is shown below, each addressing different constraints and objectives to optimize the scheduling process.

## The Maximum Lateness $\big(L_{\max}\big)$
Basically, it prioritizes tasks with the **earliest due dates**, ensuring they are completed first to reduce the chances of delays and minimize $L_{\max}$.

We have two specific subproblems related. Each subproblem focuses on different constraints and objectives for optimizing scheduling on a single machine, which are outlined below:

- [EDD algorithm](single-machine/lateness/edd.md#edd-algorithm)
- [Independence jobs](single-machine/lateness/edd.md#independence-jobs)
- [Release jobs](single-machine/lateness/edd.md#release-jobs)
## The Total (Weighted) Completion Time $\big(\sum w_j C_j\big)$

This problem aim to minimize the average waiting time $\overline{W}$ and the total completion time $\sum C_j$ or $\sum w_j C_j$ (if weights $w_j$ are present) by **prioritizing tasks** with the **shortest processing times**.

We have three specific subproblems related. Each subproblem also focuses on different constraints and objectives for optimizing scheduling on a single machine, which are outlined below:

- [SWP/WSPT algorithm](single-machine/completion/wspt.md#wspt-algorithm)
- [Independence jobs (``show_mytime``)](single-machine/completion/wspt.md#independence-jobs)
- [Sequence jobs](single-machine/completion/wspt.md#sequence-jobs)
- [Release jobs](single-machine/completion/wspt.md#release-jobs)

## References

[1] Le Minh Huy. *Single Machine Scheduling*.

[2] Michael Pinedo. *Scheduling: Theory, Algorithms, And Systems*. 01 2008.

[3] M.L. Pinedo. *Planning and Scheduling in Manufacturing and Services*. Springer series in operations research. Springer New York, 2009.

[4] PMI, editor. *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. Project Management Institute, Newtown Square, PA, 5th edition, 2013.

[5] Krzysztof Postek, Alessandro Zocca, Joaquim Gromicho, and Jeffrey Kantor. *Hands-On Mathematical Optimization with AMPL in Python*. Online, 2024.