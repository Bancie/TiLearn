---
hide:
  - navigation
---
# tilearn.show_mytime

!!! info
    For a more in-depth understanding of the concept, you can check [here](../tutorial/single-machine/completion/index.md#the-total-weighted-completion-time--show_mytime).

## tilearn.<span style="color:#ffde59;">show_mytime</span>(*list, due date*)

### Paramenter:
- **list: list or an array, that holds the job table data.**

    Each element in this collection should represent a job name, including relevant attributes such as job ID, quantity, start time, end time, and priority. These attributes are necessary for scheduling the jobs. See [notes](#notes) for a more detailed explanation of which elements in the array need to be used.



- **due date : deadline by which all jobs in the provided list need to be completed.**
  
    It represents a specific date and time and is crucial for scheduling purposes. The function will use this date to determine whether each job can be completed on time or if adjustments need to be made to meet this deadline. The due date should be formatted correctly to ensure accurate comparisons and calculations within the function.

### Notes

### Examples