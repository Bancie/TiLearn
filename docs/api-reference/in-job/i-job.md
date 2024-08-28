---
hide:
  - navigation
---
# tilearn.show_mytime

!!! info
    For a more in-depth understanding of the concept, you can check [here](../../tutorial/single-machine/completion/index.md#the-total-weighted-completion-time--show_mytime).

## tilearn.<span style="color:#ffde59;">show_mytime</span>(*list, due date*)

- **Paramenter:**

    - **list: list or an array, that holds the job table data.**

        Each element in this collection should represent a job name, including relevant attributes such as job ID, quantity, release time, due date, and priority. These attributes are necessary for scheduling the jobs. See [notes](#notes) for a more detailed explanation of which elements in the array need to be used.

    - **due date : deadline by which all jobs in the provided list need to be completed.**
      
        It represents a specific date and time and is crucial for scheduling purposes. The function will use this date to determine whether each job can be completed on time or if adjustments need to be made to meet this deadline. The due date should be formatted correctly to ensure accurate comparisons and calculations within the function.

### Notes
<figure markdown="span">
  ![alt text](job_example.png#only-light){ width="400" }
  ![alt text](job-example-white.png#only-dark){ width="400" }
  <figcaption>List example.</figcaption>
</figure>

Explanation:

| Column position | Meaning |
| :----------: |  ---------- |
| The first column | Indicates the job name. |
| The second column | Displays the quantity required to complete each job. For example, Job 1 requires 12 units to be finished. The unit type is not crucial; it is up to your discretion and it simply serves as a value for determining how weighty the job is. (e.g. 12 *minutes*, 12 *pages* for reading,...) |
| The third column | Details the release time of each job. For example, Job 1 is released on day 0. |
| The fourth column | Specifies the due date of each job. For example, Job 1 is due on day 30. |
| The last column | Exhibits the job’s weight (representing job’s priority value, you can assign weight values from 1 to 3 or 1 to 10, based on your judgment), if all jobs have equal priority, their weights would be 1. For example, the priority of Job 1 is 2. |


### Examples