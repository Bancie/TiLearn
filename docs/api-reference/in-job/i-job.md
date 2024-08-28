# tilearn.show_mytime

!!! info
    For a more in-depth understanding of the concept, you can check [here](../../user-guide/single-machine/completion/index.md#the-total-weighted-completion-time--show_mytime).

## tilearn.<span style="color:#ffde59;">show_mytime</span>(*list, due date*)

- **Paramenter:**

    - **list: list or an array, that holds the job table data.**

        Each element in this collection should represent a job name, including relevant attributes such as job ID, quantity, release time, due date, and priority. These attributes are necessary for scheduling the jobs. See [notes](#notes) for a more detailed explanation of which elements in the array need to be used.

    - **due date : deadline by which all jobs in the provided list need to be completed.**
      
        It represents a specific date and time and is crucial for scheduling purposes. The function will use this date to determine whether each job can be completed on time or if adjustments need to be made to meet this deadline. The due date should be formatted correctly to ensure accurate comparisons and calculations within the function.

### Notes

The list is a key function that displays your job data.

See the example below for more details:

<figure markdown="span">
  ![alt text](job-light.png#only-dark){ width="400" }
  ![alt text](job-dark.png#only-light){ width="400" }
  <figcaption>List example.</figcaption>
</figure>

Explanation:

<table>
  <thead>
    <tr>
      <th style="width: 200px; text-align: center;">Column position</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">The first column</td>
      <td>Indicates the job name.</td>
    </tr>
    <tr>
      <td style="text-align: center;">The second column</td>
      <td>Displays the quantity required to complete each job. For example, Job 1 requires 12 units to be finished. The unit type is not crucial; it is up to your discretion and it simply serves as a value for determining how weighty the job is. (e.g. 12 <em>minutes</em>, 12 <em>pages</em> for reading,...)</td>
    </tr>
    <tr>
      <td style="text-align: center;">The third column</td>
      <td>Details the release time of each job. For example, Job 1 is released on day 0.</td>
    </tr>
    <tr>
      <td style="text-align: center;">The fourth column</td>
      <td>Specifies the due date of each job. For example, Job 1 is due on day 30.</td>
    </tr>
    <tr>
      <td style="text-align: center;">The last column</td>
      <td>Exhibits the job’s weight (representing job’s priority value, you can assign weight values from 1 to 3 or 1 to 10, based on your judgment). The higher the priority value, the more important it is, if all jobs have equal priority, their weights would be 1. For example, the priority of Job 1 is 2.</td>
    </tr>
  </tbody>
</table>

### Examples
Code Implementation:

```py
import tilearn as tl

data = [['Job 1', 4, 0, 10, 1], ['Job 2', 9, 0, 10, 3], ['Job 3', 6, 0, 10, 2], ['Job 4', 7, 0, 10, 3], ['Job 5', 4, 0, 10, 2], ['Job 6', 5, 0, 10, 1], ['Job 7', 8, 0, 10, 3], ['Job 8', 3, 0, 10, 1], ['Job 9', 2, 0, 10, 1], ['Job 10', 6, 0, 10, 2]]

print(tl.show_mytime(data, 10))
```
*Output:*
```output
[['Job 5', 4, 0, 10, 2, 0.7407407407407407, 2.7], ['Job 9', 2, 0, 10, 1, 0.37037037037037035, 2.7], ['Job 4', 7, 0, 10, 3, 1.2962962962962963, 2.3142857142857145], ['Job 7', 8, 0, 10, 3, 1.4814814814814814, 2.025], ['Job 2', 9, 0, 10, 3, 1.6666666666666667, 1.7999999999999998], ['Job 3', 6, 0, 10, 2, 1.1111111111111112, 1.7999999999999998], ['Job 8', 3, 0, 10, 1, 0.5555555555555556, 1.7999999999999998], ['Job 10', 6, 0, 10, 2, 1.1111111111111112, 1.7999999999999998], ['Job 1', 4, 0, 10, 1, 0.7407407407407407, 1.35], ['Job 6', 5, 0, 10, 1, 0.9259259259259259, 1.08]]
```

To make the output more readable, you can adjust your code as shown below:

```py
schedule = tl.show_mytime(data, 10)

for row in schedule:
    print(row)
```
*Output:*
```output
['Job 5', 4, 0, 10, 2, 0.7407407407407407, 2.7]
['Job 9', 2, 0, 10, 1, 0.37037037037037035, 2.7]
['Job 4', 7, 0, 10, 3, 1.2962962962962963, 2.3142857142857145]
['Job 7', 8, 0, 10, 3, 1.4814814814814814, 2.025]
['Job 2', 9, 0, 10, 3, 1.6666666666666667, 1.7999999999999998]
['Job 3', 6, 0, 10, 2, 1.1111111111111112, 1.7999999999999998]
['Job 8', 3, 0, 10, 1, 0.5555555555555556, 1.7999999999999998]
['Job 10', 6, 0, 10, 2, 1.1111111111111112, 1.7999999999999998]
['Job 1', 4, 0, 10, 1, 0.7407407407407407, 1.35]
['Job 6', 5, 0, 10, 1, 0.9259259259259259, 1.08]
```