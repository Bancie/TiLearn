# The Total Weighted Completion Time $\big(\sum w_j C_j\big)$ [(``show_mytime``)](../../../api-reference/i-job.md)
## What is the main goal?

- Another optimal approach in single machine scheduling is the **Shortest Process Time (SPT)** algorithm and the **Weighted Shortest Process Time (WSPT)** algorithm.
- Both algorithms aim to minimize the average waiting time $\overline{W}$ and the total completion time $\sum C_j$ or $\sum w_j C_j$ (if weights $w_j$ are present) by prioritizing tasks with the shortest processing times.

## WSPT Algorithm

!!! note
    The problem $1\| \sum C_j$ is a special case of $1\| \sum w_j C_j$ with weights $w_j = 1$. Thus, SPT is the same as WSPT when $w_j = 1$, allowing us to focus on $1\| \sum w_j C_j$.