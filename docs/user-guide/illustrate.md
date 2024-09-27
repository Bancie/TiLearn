# Running Illustrative Data Using the TiLearn Library
## Introduction to the TiLearn 1.0.0 Library

TiLearn /taɪˈlɜrn/ is a combination of “Time” and “Machine Learning.” The library was built with the initial goal of automating the process of evaluating job weights ($w_j$) and improving the branching process (Learning to Branch) through machine learning methods.

The source code has been uploaded to GitHub, and the link is provided below.

GitHub link: [https://github.com/Bancie/TiLearn](https://github.com/Bancie/TiLearn)

The library has also been published on PyPI and can be easily downloaded and used.

Link: [https://pypi.org/project/TiLearn/](https://pypi.org/project/TiLearn/)

Additionally, the document site is designed to provide usage guides, instructions on how to run the library, and how it works.

Documentation link: [https://bancie.github.io/TiLearn/](https://bancie.github.io/TiLearn/)

The library currently supports the following features:
- A function for running the EDD algorithm.

- A function for running the WSPT algorithm.

- A function for solving the problem $1||\sum C_j$.

- A function for solving the problem $1||\sum w_j C_j$.

- A function for solving the problem $1|prec|\sum C_j$.

- A function for solving the problem $1|prec|\sum w_j C_j$.

- A function for handling a mixture of both $1|prec|\sum w_j C_j$ and $1||\sum w_j C_j$ problems.

Detailed guides on how to use these functions, including parameters and the meaning of each parameter, will be updated on the [API reference](../api-reference/index.md).

To use the library, it can be installed with the following command


```python
%pip install tilearn
```

Some supporting libraries for analysis


```python
%pip install pandas
%pip install ipython
%pip install jinja2
```

Declare the main library


```python
import tilearn as tl
from tilearn import _plat as pl
```

Some supporting libraries for data analysis


```python
import csv
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
```

## Running Illustrative Data Using TiLearn

Suppose we need to process the following three lists

- List 1:


```python
list1 = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/list1.csv'
display(pd.read_csv(list1))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Job 1</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Job 2</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Job 3</td>
      <td>3</td>
      <td>0</td>
      <td>100</td>
      <td>0.46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Job 4</td>
      <td>3</td>
      <td>0</td>
      <td>100</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Job 5</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.17</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Job 6</td>
      <td>3</td>
      <td>0</td>
      <td>100</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Job 7</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Job 8</td>
      <td>2</td>
      <td>0</td>
      <td>100</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Job 9</td>
      <td>5</td>
      <td>0</td>
      <td>100</td>
      <td>0.52</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Job 10</td>
      <td>2</td>
      <td>0</td>
      <td>100</td>
      <td>0.40</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Job 11</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Job 12</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.39</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Job 13</td>
      <td>2</td>
      <td>0</td>
      <td>100</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Job 14</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.90</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Job 15</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.22</td>
    </tr>
  </tbody>
</table>
</div>


- List 2:


```python
list2 = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/list2.csv'
display(pd.read_csv(list2))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Job 16</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Job 17</td>
      <td>3</td>
      <td>0</td>
      <td>100</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Job 18</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Job 19</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Job 20</td>
      <td>5</td>
      <td>0</td>
      <td>100</td>
      <td>0.94</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Job 21</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Job 22</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.47</td>
    </tr>
  </tbody>
</table>
</div>


- List 3:


```python
list3 = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/list3.csv'
display(pd.read_csv(list3))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Job 23</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Job 24</td>
      <td>1</td>
      <td>0</td>
      <td>100</td>
      <td>0.54</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Job 25</td>
      <td>2</td>
      <td>0</td>
      <td>100</td>
      <td>0.81</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Job 26</td>
      <td>2</td>
      <td>0</td>
      <td>100</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Job 27</td>
      <td>5</td>
      <td>0</td>
      <td>100</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Job 28</td>
      <td>2</td>
      <td>0</td>
      <td>100</td>
      <td>0.29</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Job 29</td>
      <td>5</td>
      <td>0</td>
      <td>100</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Job 30</td>
      <td>4</td>
      <td>0</td>
      <td>100</td>
      <td>0.69</td>
    </tr>
  </tbody>
</table>
</div>


In List 1, the jobs are independent and have no precedence, meaning they follow the structure of $1||\sum w_j C_j$. However, Lists 2 and 3 follow a structure that includes precedence constraints, $1|prec|\sum w_j C_j$.

The folder structure is set up as follows

```txt
tilearn/
├── main.py
└── data/
    ├── backup/
    ├── list1.csv
    ├── list2.csv
    └── list3.csv
```

Define the data paths


```python
original = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data'
backup = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/backup'
```

Select the problem type for each list by setting ``prec`` as follows:
    
- ``prec=0`` for problems that do not require job precedence.

- ``prec=1`` for problems that require job precedence.


```python
lists = [
    pl.List(file_path=list1, prec=0),
    pl.List(file_path=list2, prec=1),
    pl.List(file_path=list3, prec=1),
]
```

Run the program with the following command


```python
schedule = tl.optimal_list(lists, original, backup)
print(schedule)
```

    [['Job 14', 1.0, 0, 100, 0.9, 0.9], ['Job 2', 1.0, 0, 100, 0.84, 0.84], ['Job 12', 1.0, 0, 100, 0.39, 0.39], ['Job 13', 2.0, 0, 100, 0.57, 0.285], ['Job 4', 3.0, 0, 100, 0.79, 0.26333333333333336], ['Job 7', 4.0, 0, 100, 0.95, 0.2375], ['Job 16', 4.0, 0, 100, 0.7, 0.175], ['Job 17', 3.0, 0, 100, 0.95, 0.2357142857142857], ['Job 23', 4.0, 0, 100, 0.24, 0.06], ['Job 24', 1.0, 0, 100, 0.54, 0.156], ['Job 25', 2.0, 0, 100, 0.81, 0.22714285714285715], ['Job 15', 1.0, 0, 100, 0.22, 0.22], ['Job 26', 2.0, 0, 100, 0.41, 0.205], ['Job 10', 2.0, 0, 100, 0.4, 0.2], ['Job 18', 4.0, 0, 100, 0.49, 0.1225], ['Job 19', 1.0, 0, 100, 0.13, 0.124], ['Job 20', 5.0, 0, 100, 0.94, 0.156], ['Job 21', 1.0, 0, 100, 0.57, 0.19363636363636363], ['Job 5', 1.0, 0, 100, 0.17, 0.17], ['Job 6', 3.0, 0, 100, 0.5, 0.16666666666666666], ['Job 1', 4.0, 0, 100, 0.65, 0.1625], ['Job 3', 3.0, 0, 100, 0.46, 0.15333333333333335], ['Job 11', 4.0, 0, 100, 0.55, 0.1375], ['Job 22', 4.0, 0, 100, 0.47, 0.1175], ['Job 27', 5.0, 0, 100, 0.22, 0.044], ['Job 28', 2.0, 0, 100, 0.29, 0.07285714285714286], ['Job 29', 5.0, 0, 100, 0.65, 0.09666666666666668], ['Job 30', 4.0, 0, 100, 0.69, 0.115625], ['Job 9', 5.0, 0, 100, 0.52, 0.10400000000000001], ['Job 8', 2.0, 0, 100, 0.14, 0.07]]


To make the list more readable, you can use the following command


```python
header = ['Name','p','r','d','w','p-factor']
output = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput.csv'
schedule = tl.optimal_list(lists, original, backup)
with open(output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(schedule)
```

View the output data from the ``output.csv`` file:


```python
display(pd.read_csv('/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput.csv'))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
      <th>p-factor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Job 14</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.90</td>
      <td>0.900000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Job 2</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.84</td>
      <td>0.840000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Job 12</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.39</td>
      <td>0.390000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Job 13</td>
      <td>2.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.57</td>
      <td>0.285000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Job 4</td>
      <td>3.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.79</td>
      <td>0.263333</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Job 7</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.95</td>
      <td>0.237500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Job 16</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.70</td>
      <td>0.175000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Job 17</td>
      <td>3.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.95</td>
      <td>0.235714</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Job 23</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.24</td>
      <td>0.060000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Job 24</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.54</td>
      <td>0.156000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Job 25</td>
      <td>2.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.81</td>
      <td>0.227143</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Job 15</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.22</td>
      <td>0.220000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Job 26</td>
      <td>2.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.41</td>
      <td>0.205000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Job 10</td>
      <td>2.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.40</td>
      <td>0.200000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Job 18</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.49</td>
      <td>0.122500</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Job 19</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.13</td>
      <td>0.124000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Job 20</td>
      <td>5.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.94</td>
      <td>0.156000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Job 21</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.57</td>
      <td>0.193636</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Job 5</td>
      <td>1.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.17</td>
      <td>0.170000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Job 6</td>
      <td>3.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.50</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Job 1</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.65</td>
      <td>0.162500</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Job 3</td>
      <td>3.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.46</td>
      <td>0.153333</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Job 11</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.55</td>
      <td>0.137500</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Job 22</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.47</td>
      <td>0.117500</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Job 27</td>
      <td>5.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.22</td>
      <td>0.044000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Job 28</td>
      <td>2.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.29</td>
      <td>0.072857</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Job 29</td>
      <td>5.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.65</td>
      <td>0.096667</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Job 30</td>
      <td>4.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.69</td>
      <td>0.115625</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Job 9</td>
      <td>5.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.52</td>
      <td>0.104000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Job 8</td>
      <td>2.0</td>
      <td>0</td>
      <td>100</td>
      <td>0.14</td>
      <td>0.070000</td>
    </tr>
  </tbody>
</table>
</div>


### Data Analysis

We use the `pandas` library to help visualize the data.


```python
df = pd.read_csv(r'/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput.csv', engine='pyarrow')
```

Let’s first look at the processing time chart


```python
plt.figure(figsize=(7, 3))
df['p'].plot(title='Processing Time Chart')
plt.show()
```


    
![png](Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_files/Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_39_0.png)
    


Based on the chart above, we can see that after optimizing the job list, the processing times for each job tend to increase from the first job to the last job.

Next, let’s look at the job weight chart


```python
plt.figure(figsize=(7, 3))
df['w'].plot(title='Job Weight Chart')
plt.show()
```


    
![png](Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_files/Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_42_0.png)
    


From this chart, we can see that after optimizing the job list, the weights of each job tend to decrease from the first job to the last job.

From these insights, it is easy to observe that jobs with shorter processing times and higher priority weights are pushed to the top, while jobs with longer processing times and lower priorities are placed at the bottom.

## Scheduling for Design Production Using TiLearn

### Introduction to the Design Process

In the processing stage, studios often face the challenge of allocating resources and adjusting designs for multiple projects simultaneously. This is based on client priority, the complexity of each project, and external factors such as construction time. Applying scheduling techniques helps manage data more efficiently, plan better, and track progress while adjusting when necessary.

Typically, an interior design project goes through the following main stages:

Concept development
- Space planning
- Design development
- Material selection
- Cost estimation
- Construction
- Installation
- Decoration
- Handover

Each phase needs to be completed before moving to the next. Therefore, the problem can be modeled as a scheduling problem with precedence constraints: $1|prec|\sum w_j C_j$, where tasks must follow priority and precedence rules.

Additionally, the studio may need to perform condition surveys for various projects, which do not require sequential completion. In this case, the problem can be modeled as $1||\sum w_j C_j$, where jobs can be completed in any order.

### Running Illustrative Data

Suppose we have the following three projects: A, B, and C

Project A:


```python
project_A = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Project-A.csv'
display(pd.read_csv(project_A))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Project A - Concept development</td>
      <td>4</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Project A - Space planning</td>
      <td>3</td>
      <td>0</td>
      <td>200</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Project A - Design development</td>
      <td>5</td>
      <td>0</td>
      <td>200</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Project A - Material selection</td>
      <td>2</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Project A - Cost estimation</td>
      <td>2</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Project A - Construction</td>
      <td>10</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Project A - Installation</td>
      <td>4</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Project A - Decoration</td>
      <td>3</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Project A - Handover</td>
      <td>1</td>
      <td>0</td>
      <td>200</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>


Project B:


```python
project_B = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Project-B.csv'
display(pd.read_csv(project_B))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Project B - Concept development</td>
      <td>8</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Project B - Space planning</td>
      <td>7</td>
      <td>0</td>
      <td>200</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Project B - Design development</td>
      <td>20</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Project B - Material selection</td>
      <td>3</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Project B - Cost estimation</td>
      <td>2</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Project B - Construction</td>
      <td>40</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Project B - Installation</td>
      <td>15</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Project B - Decoration</td>
      <td>9</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Project B - Handover</td>
      <td>1</td>
      <td>0</td>
      <td>200</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>


Project C:


```python
project_C = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Project-C.csv'
display(pd.read_csv(project_C))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Project C - Concept development</td>
      <td>5</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Project C - Space planning</td>
      <td>2</td>
      <td>0</td>
      <td>200</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Project C - Design development</td>
      <td>4</td>
      <td>0</td>
      <td>200</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Project C - Material selection</td>
      <td>6</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Project C - Cost estimation</td>
      <td>1</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Project C - Construction</td>
      <td>15</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Project C - Installation</td>
      <td>4</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Project C - Decoration</td>
      <td>4</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Project C - Handover</td>
      <td>1</td>
      <td>0</td>
      <td>200</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>


The list of locations requiring a survey:


```python
survey = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Survey.csv'
display(pd.read_csv(survey))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Survey Location 1</td>
      <td>2</td>
      <td>0</td>
      <td>200</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Survey Location 2</td>
      <td>6</td>
      <td>0</td>
      <td>200</td>
      <td>0.67</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Survey Location 3</td>
      <td>5</td>
      <td>0</td>
      <td>200</td>
      <td>0.45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Survey Location 4</td>
      <td>15</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Survey Location 5</td>
      <td>4</td>
      <td>0</td>
      <td>200</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Survey Location 6</td>
      <td>4</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Survey Location 7</td>
      <td>20</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
    </tr>
  </tbody>
</table>
</div>


The folder structure is set up as follows:

```txt
tilearn/
├── main.py
└── data_project/
    ├── backup/
    ├── Project-A.csv
    ├── Project-B.csv
    ├── Project-C.csv
    └── Survey.csv
```

Define the data paths


```python
original_project = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project'
backup_project = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/backup'
```

The survey list does not require sequential completion, so `prec=0`. However, for projects A, B, and C, jobs require sequential completion, so `prec=1` for all of them.


```python
lists_project = [
    pl.List(file_path=survey, prec=0),
    pl.List(file_path=project_A, prec=1),
    pl.List(file_path=project_B, prec=1),
    pl.List(file_path=project_C, prec=1),
]
```

Run the program with the following command


```python
header = ['Name','p','r','d','w','p-factor']
output = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput_project.csv'
schedule = tl.optimal_list(lists_project, original_project, backup_project)
with open(output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(schedule)
```

You can view the output data from the `output_project.csv` file


```python
display(pd.read_csv('/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput_project.csv'))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>p</th>
      <th>r</th>
      <th>d</th>
      <th>w</th>
      <th>p-factor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Project A - Concept development</td>
      <td>4.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
      <td>0.212500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Project A - Space planning</td>
      <td>3.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.80</td>
      <td>0.235714</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Project C - Concept development</td>
      <td>5.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
      <td>0.170000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Project C - Space planning</td>
      <td>2.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.80</td>
      <td>0.235714</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Project A - Design development</td>
      <td>5.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.75</td>
      <td>0.150000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Project A - Material selection</td>
      <td>2.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
      <td>0.207143</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Project A - Cost estimation</td>
      <td>2.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
      <td>0.227778</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Project A - Construction</td>
      <td>10.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
      <td>0.095000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Project A - Installation</td>
      <td>4.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
      <td>0.117857</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Project A - Decoration</td>
      <td>3.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
      <td>0.147059</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Project A - Handover</td>
      <td>1.0</td>
      <td>0</td>
      <td>200</td>
      <td>1.00</td>
      <td>0.194444</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Project C - Design development</td>
      <td>4.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.75</td>
      <td>0.187500</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Project C - Material selection</td>
      <td>6.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
      <td>0.116667</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Project C - Cost estimation</td>
      <td>1.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
      <td>0.185714</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Survey Location 1</td>
      <td>2.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.33</td>
      <td>0.165000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Survey Location 6</td>
      <td>4.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
      <td>0.150000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Project C - Construction</td>
      <td>15.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
      <td>0.063333</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Project C - Installation</td>
      <td>4.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
      <td>0.086842</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Project C - Decoration</td>
      <td>4.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
      <td>0.108696</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Project C - Handover</td>
      <td>1.0</td>
      <td>0</td>
      <td>200</td>
      <td>1.00</td>
      <td>0.145833</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Survey Location 2</td>
      <td>6.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.67</td>
      <td>0.111667</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Project B - Concept development</td>
      <td>8.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
      <td>0.106250</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Project B - Space planning</td>
      <td>7.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.80</td>
      <td>0.110000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Survey Location 3</td>
      <td>5.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.45</td>
      <td>0.090000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Project B - Design development</td>
      <td>20.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
      <td>0.047500</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Project B - Material selection</td>
      <td>3.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
      <td>0.071739</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Project B - Cost estimation</td>
      <td>2.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.60</td>
      <td>0.090000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Survey Location 4</td>
      <td>15.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
      <td>0.056667</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Project B - Construction</td>
      <td>40.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.95</td>
      <td>0.023750</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Project B - Installation</td>
      <td>15.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
      <td>0.030000</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Project B - Decoration</td>
      <td>9.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.85</td>
      <td>0.039062</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Project B - Handover</td>
      <td>1.0</td>
      <td>0</td>
      <td>200</td>
      <td>1.00</td>
      <td>0.053846</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Survey Location 7</td>
      <td>20.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.70</td>
      <td>0.035000</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Survey Location 5</td>
      <td>4.0</td>
      <td>0</td>
      <td>200</td>
      <td>0.10</td>
      <td>0.025000</td>
    </tr>
  </tbody>
</table>
</div>


### Data Visualization

We use the `pandas` library to help visualize the data for the design processing task


```python
df_project = pd.read_csv(r'/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput_project.csv', engine='pyarrow')
plt.figure(figsize=(5, 2.4))
df_project['p'].plot(title='Processing Time Chart')
plt.show()
```


    
![png](Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_files/Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_70_0.png)
    



```python
plt.figure(figsize=(5, 2.4))
df_project['w'].plot(title='Job Weight Chart')
plt.show()
```


    
![png](Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_files/Running%20Illustrative%20Data%20Using%20the%20TiLearn%20Library_71_0.png)
    

