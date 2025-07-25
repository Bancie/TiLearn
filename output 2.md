:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
# Introduction to the TiLearn Library[¶](#Introduction-to-the-TiLearn-Library){.anchor-link} {#Introduction-to-the-TiLearn-Library}
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
TiLearn /taɪˈlɜrn/ is a combination of "Time" and "Machine Learning."
The library was built with the initial goal of automating the process of
evaluating job weights (\$w_j\$) and improving the branching process
(Learning to Branch) through machine learning methods.

The source code has been uploaded to GitHub, and the link is provided
below.

GitHub link: <https://github.com/Bancie/TiLearn>
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
The library has also been published on PyPI and can be easily downloaded
and used.

Link: <https://pypi.org/project/TiLearn/>
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Additionally, the document site is designed to provide usage guides,
instructions on how to run the library, and how it works.

Documentation link: <https://bancie.github.io/TiLearn/>
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
The library currently supports the following features:

-   A function for running the EDD algorithm.

-   A function for running the WSPT algorithm.

-   A function for solving the problem \$1\|\|\\sum C_j\$.

-   A function for solving the problem \$1\|\|\\sum w_j C_j\$.

-   A function for solving the problem \$1\|prec\|\\sum C_j\$.

-   A function for solving the problem \$1\|prec\|\\sum w_j C_j\$.

-   A function for handling a mixture of both \$1\|prec\|\\sum w_j C_j\$
    and \$1\|\|\\sum w_j C_j\$ problems.
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Detailed guides on how to use these functions, including parameters and
the meaning of each parameter, will be updated on the [documentation
site](https://bancie.github.io/TiLearn/).
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
To use the library, it can be installed with the following command
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    %pip install tilearn
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Some supporting libraries for analysis
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    %pip install pandas
    %pip install ipython
    %pip install jinja2
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Declare the main library
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[4\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import tilearn as tl
    from tilearn import _plat as pl
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Some supporting libraries for data analysis
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[5\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import csv
    import pandas as pd
    from IPython.display import display
    import matplotlib.pyplot as plt
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
# Running Illustrative Data Using TiLearn[¶](#Running-Illustrative-Data-Using-TiLearn){.anchor-link} {#Running-Illustrative-Data-Using-TiLearn}
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Suppose we need to process the following three lists
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
-   List 1:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[6\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    list1 = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/list1.csv'
    display(pd.read_csv(list1))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

       Name     p   r   d     w
  ---- -------- --- --- ----- ------
  0    Job 1    4   0   100   0.65
  1    Job 2    1   0   100   0.84
  2    Job 3    3   0   100   0.46
  3    Job 4    3   0   100   0.79
  4    Job 5    1   0   100   0.17
  5    Job 6    3   0   100   0.50
  6    Job 7    4   0   100   0.95
  7    Job 8    2   0   100   0.14
  8    Job 9    5   0   100   0.52
  9    Job 10   2   0   100   0.40
  10   Job 11   4   0   100   0.55
  11   Job 12   1   0   100   0.39
  12   Job 13   2   0   100   0.57
  13   Job 14   1   0   100   0.90
  14   Job 15   1   0   100   0.22

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
-   List 2:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[7\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    list2 = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/list2.csv'
    display(pd.read_csv(list2))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

      Name     p   r   d     w
  --- -------- --- --- ----- ------
  0   Job 16   4   0   100   0.70
  1   Job 17   3   0   100   0.95
  2   Job 18   4   0   100   0.49
  3   Job 19   1   0   100   0.13
  4   Job 20   5   0   100   0.94
  5   Job 21   1   0   100   0.57
  6   Job 22   4   0   100   0.47

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
-   List 3:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[8\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    list3 = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/list3.csv'
    display(pd.read_csv(list3))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

      Name     p   r   d     w
  --- -------- --- --- ----- ------
  0   Job 23   4   0   100   0.24
  1   Job 24   1   0   100   0.54
  2   Job 25   2   0   100   0.81
  3   Job 26   2   0   100   0.41
  4   Job 27   5   0   100   0.22
  5   Job 28   2   0   100   0.29
  6   Job 29   5   0   100   0.65
  7   Job 30   4   0   100   0.69

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
In List 1, the jobs are independent and have no precedence, meaning they
follow the structure of \$1\|\|\\sum w_j C_j\$. However, Lists 2 and 3
follow a structure that includes precedence constraints,
\$1\|prec\|\\sum w_j C_j\$.
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
The folder structure is set up as follows
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
``` txt
txt
tilearn/
├── main.py
└── data/
    ├── backup/
    ├── list1.csv
    ├── list2.csv
    └── list3.csv
```
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Define the data paths
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[9\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    original = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data'
    backup = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data/backup'
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Select the problem type for each list by setting `prec` as follows:

-   `prec=0` for problems that do not require job precedence.

-   `prec=1` for problems that require job precedence.
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[10\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    lists = [
        pl.List(file_path=list1, prec=0),
        pl.List(file_path=list2, prec=1),
        pl.List(file_path=list3, prec=1),
    ]
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Run the program with the following command
:::
:::::
:::::::
::::::::

:::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[11\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    schedule = tl.optimal_list(lists, original, backup)
    print(schedule)
:::
::::
:::::
:::::::
:::::::::

:::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

:::::: {.jp-OutputArea .jp-Cell-outputArea}
::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedText .jp-OutputArea-output mime-type="text/plain" tabindex="0"}
    [['Job 14', 1.0, 0, 100, 0.9, 0.9], ['Job 2', 1.0, 0, 100, 0.84, 0.84], ['Job 12', 1.0, 0, 100, 0.39, 0.39], ['Job 13', 2.0, 0, 100, 0.57, 0.285], ['Job 4', 3.0, 0, 100, 0.79, 0.26333333333333336], ['Job 7', 4.0, 0, 100, 0.95, 0.2375], ['Job 16', 4.0, 0, 100, 0.7, 0.175], ['Job 17', 3.0, 0, 100, 0.95, 0.2357142857142857], ['Job 23', 4.0, 0, 100, 0.24, 0.06], ['Job 24', 1.0, 0, 100, 0.54, 0.156], ['Job 25', 2.0, 0, 100, 0.81, 0.22714285714285715], ['Job 15', 1.0, 0, 100, 0.22, 0.22], ['Job 26', 2.0, 0, 100, 0.41, 0.205], ['Job 10', 2.0, 0, 100, 0.4, 0.2], ['Job 18', 4.0, 0, 100, 0.49, 0.1225], ['Job 19', 1.0, 0, 100, 0.13, 0.124], ['Job 20', 5.0, 0, 100, 0.94, 0.156], ['Job 21', 1.0, 0, 100, 0.57, 0.19363636363636363], ['Job 5', 1.0, 0, 100, 0.17, 0.17], ['Job 6', 3.0, 0, 100, 0.5, 0.16666666666666666], ['Job 1', 4.0, 0, 100, 0.65, 0.1625], ['Job 3', 3.0, 0, 100, 0.46, 0.15333333333333335], ['Job 11', 4.0, 0, 100, 0.55, 0.1375], ['Job 22', 4.0, 0, 100, 0.47, 0.1175], ['Job 27', 5.0, 0, 100, 0.22, 0.044], ['Job 28', 2.0, 0, 100, 0.29, 0.07285714285714286], ['Job 29', 5.0, 0, 100, 0.65, 0.09666666666666668], ['Job 30', 4.0, 0, 100, 0.69, 0.115625], ['Job 9', 5.0, 0, 100, 0.52, 0.10400000000000001], ['Job 8', 2.0, 0, 100, 0.14, 0.07]]
:::
:::::
::::::
::::::::
::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
To make the list more readable, you can use the following command
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[12\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    header = ['Name','p','r','d','w','p-factor']
    output = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput.csv'
    schedule = tl.optimal_list(lists, original, backup)
    with open(output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(schedule)
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
View the output data from the `output.csv` file:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[13\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    display(pd.read_csv('/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput.csv'))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

       Name     p     r   d     w      p-factor
  ---- -------- ----- --- ----- ------ ----------
  0    Job 14   1.0   0   100   0.90   0.900000
  1    Job 2    1.0   0   100   0.84   0.840000
  2    Job 12   1.0   0   100   0.39   0.390000
  3    Job 13   2.0   0   100   0.57   0.285000
  4    Job 4    3.0   0   100   0.79   0.263333
  5    Job 7    4.0   0   100   0.95   0.237500
  6    Job 16   4.0   0   100   0.70   0.175000
  7    Job 17   3.0   0   100   0.95   0.235714
  8    Job 23   4.0   0   100   0.24   0.060000
  9    Job 24   1.0   0   100   0.54   0.156000
  10   Job 25   2.0   0   100   0.81   0.227143
  11   Job 15   1.0   0   100   0.22   0.220000
  12   Job 26   2.0   0   100   0.41   0.205000
  13   Job 10   2.0   0   100   0.40   0.200000
  14   Job 18   4.0   0   100   0.49   0.122500
  15   Job 19   1.0   0   100   0.13   0.124000
  16   Job 20   5.0   0   100   0.94   0.156000
  17   Job 21   1.0   0   100   0.57   0.193636
  18   Job 5    1.0   0   100   0.17   0.170000
  19   Job 6    3.0   0   100   0.50   0.166667
  20   Job 1    4.0   0   100   0.65   0.162500
  21   Job 3    3.0   0   100   0.46   0.153333
  22   Job 11   4.0   0   100   0.55   0.137500
  23   Job 22   4.0   0   100   0.47   0.117500
  24   Job 27   5.0   0   100   0.22   0.044000
  25   Job 28   2.0   0   100   0.29   0.072857
  26   Job 29   5.0   0   100   0.65   0.096667
  27   Job 30   4.0   0   100   0.69   0.115625
  28   Job 9    5.0   0   100   0.52   0.104000
  29   Job 8    2.0   0   100   0.14   0.070000

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
## Data Visualization[¶](#Data-Visualization){.anchor-link} {#Data-Visualization}
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
We use the `pandas` library to help visualize the data.
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[14\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    df = pd.read_csv(r'/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput.csv', engine='pyarrow')
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Let's first look at the processing time chart
:::
:::::
:::::::
::::::::

:::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[15\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    plt.figure(figsize=(7, 3))
    df['p'].plot(title='Processing Time Chart')
    plt.show()
:::
::::
:::::
:::::::
:::::::::

:::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

:::::: {.jp-OutputArea .jp-Cell-outputArea}
::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkYAAAEpCAYAAAB2l+1+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABju0lEQVR4nO29eXwb9Z3//xpJluRD8m3Zjh0nce6TkJAQICGQwwkQCNBSjqWBdtlvu4GWArvfUr4U0rIbWmChB6X9Lv3Bt0tpoN2GdmmTEMhBKSSEQCBxLtu5E9+XZMu65/fH6DOSHB865tCM3s/Hw4/Esjzz8Wg0es37eL05nud5EARBEARBEDCovQCCIAiCIIh0gYQRQRAEQRBEGBJGBEEQBEEQYUgYEQRBEARBhCFhRBAEQRAEEYaEEUEQBEEQRBgSRgRBEARBEGFIGBEEQRAEQYQhYUQQBEEQBBGGhBFBEEnDcRyefPJJtZcxLK+++io4jsOpU6fUXkpS3HPPPcjLy1N7GQSRUZAwIogUYB+87MtqtWLy5Mm4//770draqvbydMnSpUtjjvlwX+ks2DweD55//nksXLgQ+fn5MefN8ePHVVmT2+3Gk08+iV27dqmyf4JIF0xqL4Ag9MAPfvADjB8/Hh6PBx988AFeeukl/PWvf8WhQ4eQk5Oj9vJkY2BgACaTspeRxx57DP/4j/8ofr9v3z789Kc/xfe+9z1MmzZNfHz27NmYMWMGbr/9dlgsFkXXOBIdHR1YtWoV9u/fjxtuuAF33nkn8vLycOzYMWzatAn/9//+X/h8PsXX5Xa7sWHDBgCC+CSITIWEEUFIwOrVqzF//nwAwD/+4z+iuLgY//Ef/4E//elPuOOOO4b8nf7+fuTm5iq5TMmxWq2K73PFihUXreGnP/0pVqxYMeQHutFoVGhl8XHPPffgs88+wx/+8AfceuutMT/74Q9/iMcee0zR9YRCIVWEGEGkK5RKIwgZuPbaawEAJ0+eBBCpFWlqasJ1110Hm82Gu+66C4AgkB5++GFUV1fDYrFgypQpePbZZ8Hz/EXbfe2117BgwQLk5OSgsLAQS5YswTvvvBPznC1btmDx4sXIzc2FzWbD9ddfj/r6+pjntLS04N5770VVVRUsFgsqKipw0003xdTifPLJJ6irq0NJSQmys7Mxfvx4fO1rX4vZzuCU1ZNPPgmO49DY2Ih77rkHBQUFyM/Px7333gu32x3zuwMDA/jWt76FkpIS2Gw23HjjjTh//rykabChaozGjRuHG264Abt27cL8+fORnZ2NWbNmiSmkP/7xj5g1axasVivmzZuHzz777KLtHj16FF/60pdQVFQEq9WK+fPn489//vOo69m7dy/+8pe/4Otf//pFoggALBYLnn322YseP3/+PNauXYu8vDyUlpbikUceQTAYjHnOs88+iyuuuALFxcXIzs7GvHnz8Ic//OGibXEch/vvvx+//e1vMWPGDFgsFvzyl79EaWkpAGDDhg2aSEcShFxQxIggZKCpqQkAUFxcLD4WCARQV1eHq666Cs8++yxycnLA8zxuvPFG7Ny5E1//+tdxySWXYNu2bfiXf/kXnD9/Hs8//7z4+xs2bMCTTz6JK664Aj/4wQ9gNpuxd+9e7NixAytXrgQA/Nd//RfWrVuHuro6/OhHP4Lb7cZLL72Eq666Cp999hnGjRsHALj11ltRX1+PBx54AOPGjUNbWxu2b9+OM2fOiN+vXLkSpaWl+O53v4uCggKcOnUKf/zjH+P6+2+77TaMHz8eGzduxKeffoqXX34ZZWVl+NGPfiQ+55577sGbb76Ju+++G5dffjl2796N66+/PtVDHxeNjY2488478b/+1//CP/zDP+DZZ5/FmjVr8Mtf/hLf+9738M///M8AgI0bN+K2227DsWPHYDAI95H19fW48sorMWbMGHz3u99Fbm4u3nzzTaxduxb//d//jZtvvnnY/TLxdPfdd8e91mAwiLq6OixcuBDPPvss3n33XTz33HOora3FN7/5TfF5P/nJT3DjjTfirrvugs/nw6ZNm/DlL38Zb7/99kXHdceOHXjzzTdx//33o6SkBHPmzMFLL72Eb37zm7j55ptxyy23ABDSkQSRcfAEQSTNK6+8wgPg3333Xb69vZ0/e/Ysv2nTJr64uJjPzs7mz507x/M8z69bt44HwH/3u9+N+f233nqLB8A/9dRTMY9/6Utf4jmO4xsbG3me5/mGhgbeYDDwN998Mx8MBmOeGwqFeJ7neZfLxRcUFPD33XdfzM9bWlr4/Px88fHu7m4eAP/MM88M+3dt3ryZB8Dv27dvxL8fAP/EE0+I3z/xxBM8AP5rX/tazPNuvvlmvri4WPx+//79PAD+wQcfjHnePffcc9E2R+P3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)
:::
:::::
::::::
::::::::
::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Based on the chart above, we can see that after optimizing the job list,
the processing times for each job tend to increase from the first job to
the last job.
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Next, let's look at the job weight chart
:::
:::::
:::::::
::::::::

:::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[16\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    plt.figure(figsize=(7, 3))
    df['w'].plot(title='Job Weight Chart')
    plt.show()
:::
::::
:::::
:::::::
:::::::::

:::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

:::::: {.jp-OutputArea .jp-Cell-outputArea}
::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,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)
:::
:::::
::::::
::::::::
::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
From this chart, we can see that after optimizing the job list, the
weights of each job tend to decrease from the first job to the last job.
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
From these insights, it is easy to observe that jobs with shorter
processing times and higher priority weights are pushed to the top,
while jobs with longer processing times and lower priorities are placed
at the bottom.
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
# Scheduling for Design Production Using TiLearn[¶](#Scheduling-for-Design-Production-Using-TiLearn){.anchor-link} {#Scheduling-for-Design-Production-Using-TiLearn}
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
## Introduction to the Design Process[¶](#Introduction-to-the-Design-Process){.anchor-link} {#Introduction-to-the-Design-Process}
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
In the processing stage, studios often face the challenge of allocating
resources and adjusting designs for multiple projects simultaneously.
This is based on client priority, the complexity of each project, and
external factors such as construction time. Applying scheduling
techniques helps manage data more efficiently, plan better, and track
progress while adjusting when necessary.

Typically, an interior design project goes through the following main
stages:

Concept development

-   Space planning
-   Design development
-   Material selection
-   Cost estimation
-   Construction
-   Installation
-   Decoration
-   Handover

Each phase needs to be completed before moving to the next. Therefore,
the problem can be modeled as a scheduling problem with precedence
constraints: \$1\|prec\|\\sum w_j C_j\$, where tasks must follow
priority and precedence rules.

Additionally, the studio may need to perform condition surveys for
various projects, which do not require sequential completion. In this
case, the problem can be modeled as \$1\|\|\\sum w_j C_j\$, where jobs
can be completed in any order.
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
## Running Illustrative Data[¶](#Running-Illustrative-Data){.anchor-link} {#Running-Illustrative-Data}
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Suppose we have the following three projects: A, B, and C
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Project A:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[17\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    project_A = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Project-A.csv'
    display(pd.read_csv(project_A))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

      name                              p    r   d     w
  --- --------------------------------- ---- --- ----- ------
  0   Project A - Concept development   4    0   200   0.85
  1   Project A - Space planning        3    0   200   0.80
  2   Project A - Design development    5    0   200   0.75
  3   Project A - Material selection    2    0   200   0.70
  4   Project A - Cost estimation       2    0   200   0.60
  5   Project A - Construction          10   0   200   0.95
  6   Project A - Installation          4    0   200   0.70
  7   Project A - Decoration            3    0   200   0.85
  8   Project A - Handover              1    0   200   1.00

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Project B:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[18\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    project_B = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Project-B.csv'
    display(pd.read_csv(project_B))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

      name                              p    r   d     w
  --- --------------------------------- ---- --- ----- ------
  0   Project B - Concept development   8    0   200   0.85
  1   Project B - Space planning        7    0   200   0.80
  2   Project B - Design development    20   0   200   0.95
  3   Project B - Material selection    3    0   200   0.70
  4   Project B - Cost estimation       2    0   200   0.60
  5   Project B - Construction          40   0   200   0.95
  6   Project B - Installation          15   0   200   0.70
  7   Project B - Decoration            9    0   200   0.85
  8   Project B - Handover              1    0   200   1.00

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Project C:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[19\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    project_C = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Project-C.csv'
    display(pd.read_csv(project_C))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

      name                              p    r   d     w
  --- --------------------------------- ---- --- ----- ------
  0   Project C - Concept development   5    0   200   0.85
  1   Project C - Space planning        2    0   200   0.80
  2   Project C - Design development    4    0   200   0.75
  3   Project C - Material selection    6    0   200   0.70
  4   Project C - Cost estimation       1    0   200   0.60
  5   Project C - Construction          15   0   200   0.95
  6   Project C - Installation          4    0   200   0.70
  7   Project C - Decoration            4    0   200   0.85
  8   Project C - Handover              1    0   200   1.00

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
The list of locations requiring a survey:
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[20\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    survey = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/Survey.csv'
    display(pd.read_csv(survey))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

      name                p    r   d     w
  --- ------------------- ---- --- ----- ------
  0   Survey Location 1   2    0   200   0.33
  1   Survey Location 2   6    0   200   0.67
  2   Survey Location 3   5    0   200   0.45
  3   Survey Location 4   15   0   200   0.85
  4   Survey Location 5   4    0   200   0.10
  5   Survey Location 6   4    0   200   0.60
  6   Survey Location 7   20   0   200   0.70

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
The folder structure is set up as follows:
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
``` txt
txt
tilearn/
├── main.py
└── data_project/
    ├── backup/
    ├── Project-A.csv
    ├── Project-B.csv
    ├── Project-C.csv
    └── Survey.csv
```
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Define the data paths
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[21\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    original_project = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project'
    backup_project = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/data_project/backup'
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
The survey list does not require sequential completion, so `prec=0`.
However, for projects A, B, and C, jobs require sequential completion,
so `prec=1` for all of them.
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[22\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    lists_project = [
        pl.List(file_path=survey, prec=0),
        pl.List(file_path=project_A, prec=1),
        pl.List(file_path=project_B, prec=1),
        pl.List(file_path=project_C, prec=1),
    ]
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
Run the program with the following command
:::
:::::
:::::::
::::::::

:::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[23\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    header = ['Name','p','r','d','w','p-factor']
    output = '/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput_project.csv'
    schedule = tl.optimal_list(lists_project, original_project, backup_project)
    with open(output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(schedule)
:::
::::
:::::
:::::::
:::::::::
::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
You can view the output data from the `output_project.csv` file
:::
:::::
:::::::
::::::::

::::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[24\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    display(pd.read_csv('/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput_project.csv'))
:::
::::
:::::
:::::::
:::::::::

::::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::::::: {.jp-OutputArea .jp-Cell-outputArea}
:::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

:::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output mime-type="text/html" tabindex="0"}
<div>

       Name                              p      r   d     w      p-factor
  ---- --------------------------------- ------ --- ----- ------ ----------
  0    Project A - Concept development   4.0    0   200   0.85   0.212500
  1    Project A - Space planning        3.0    0   200   0.80   0.235714
  2    Project C - Concept development   5.0    0   200   0.85   0.170000
  3    Project C - Space planning        2.0    0   200   0.80   0.235714
  4    Project A - Design development    5.0    0   200   0.75   0.150000
  5    Project A - Material selection    2.0    0   200   0.70   0.207143
  6    Project A - Cost estimation       2.0    0   200   0.60   0.227778
  7    Project A - Construction          10.0   0   200   0.95   0.095000
  8    Project A - Installation          4.0    0   200   0.70   0.117857
  9    Project A - Decoration            3.0    0   200   0.85   0.147059
  10   Project A - Handover              1.0    0   200   1.00   0.194444
  11   Project C - Design development    4.0    0   200   0.75   0.187500
  12   Project C - Material selection    6.0    0   200   0.70   0.116667
  13   Project C - Cost estimation       1.0    0   200   0.60   0.185714
  14   Survey Location 1                 2.0    0   200   0.33   0.165000
  15   Survey Location 6                 4.0    0   200   0.60   0.150000
  16   Project C - Construction          15.0   0   200   0.95   0.063333
  17   Project C - Installation          4.0    0   200   0.70   0.086842
  18   Project C - Decoration            4.0    0   200   0.85   0.108696
  19   Project C - Handover              1.0    0   200   1.00   0.145833
  20   Survey Location 2                 6.0    0   200   0.67   0.111667
  21   Project B - Concept development   8.0    0   200   0.85   0.106250
  22   Project B - Space planning        7.0    0   200   0.80   0.110000
  23   Survey Location 3                 5.0    0   200   0.45   0.090000
  24   Project B - Design development    20.0   0   200   0.95   0.047500
  25   Project B - Material selection    3.0    0   200   0.70   0.071739
  26   Project B - Cost estimation       2.0    0   200   0.60   0.090000
  27   Survey Location 4                 15.0   0   200   0.85   0.056667
  28   Project B - Construction          40.0   0   200   0.95   0.023750
  29   Project B - Installation          15.0   0   200   0.70   0.030000
  30   Project B - Decoration            9.0    0   200   0.85   0.039062
  31   Project B - Handover              1.0    0   200   1.00   0.053846
  32   Survey Location 7                 20.0   0   200   0.70   0.035000
  33   Survey Location 5                 4.0    0   200   0.10   0.025000

</div>
::::
::::::
:::::::
:::::::::
:::::::::::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
## Data Visualization[¶](#Data-Visualization){.anchor-link} {#Data-Visualization}
:::
:::::
:::::::
::::::::

:::::::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
We use the `pandas` library to help visualize the data for the design
processing task
:::
:::::
:::::::
::::::::

:::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[34\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    df_project = pd.read_csv(r'/Users/chibangnguyen/Documents/thuhoach.nckh/tilearn/ouput_project.csv', engine='pyarrow')
    plt.figure(figsize=(5, 2.4))
    df_project['p'].plot(title='Processing Time Chart')
    plt.show()
:::
::::
:::::
:::::::
:::::::::

:::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

:::::: {.jp-OutputArea .jp-Cell-outputArea}
::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,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xcXF6V1XXV2t97VSqWS9evVio0aN0rseABMKhezSpUt61xcWFpr8uydtF00tEpMlJiYiMDAQERERmDFjBjw9PbF7926EhYXp3U/3EzQA/PTTTxCJRPjb3/6md/1LL70Exhh+/vlnAMCePXug0WiwatUqPjPgCAQCAMD+/ftRWlqKJ554AkVFRfxFJBIhPj4ehw4dAgC4ublBIpHg8OHDKCkpMfh8fHx8AAA//PADVCqVyb+PBQsW6H09fPhwFBcXo7y8HADwyy+/AACf+XCWLFli8s8yR48ePZCQkMB/HR8fD0A7JRwZGdnk+ps3bwIA7t27h4MHD2L69OmoqKjgf8fFxcVISkpCZmYmcnNzm/253PP38vIyabyGfp/cmDhubm78v0tKSlBWVobhw4fj9OnTTR7vwQcfRI8ePUwaA3EuNLVITJaSkoKuXbtCLBYjODgY3bp1axJwxGIxwsPD9a7LyspCaGhokzc2rvouKysLgHaqUigUtvjmk5mZCaBhfa4xb29vANp1mDfffBMvvfQSgoODMXjwYDz66KN46qmnEBISAkD7Rjdt2jSsWbMGGzZswMiRIzF58mTMnDnTqApA3WAAAL6+vgC0b7De3t7IysqCUChEdHS03v06d+7c6mNbQ+PxyWQyAEBERITB67mAf/36dTDG8Oqrr+LVV181+NgFBQVNPsBwuNegoqKC/7DQGldXV379iuPr69vkQ8gPP/yAN954A2fPnoVCoeCv5z7o6Gr8eyftDwUyYrJBgwbxVYvNkUqlTYKbNWk0GgDadTIuIOnSLZNfunQpJkyYgD179mDfvn149dVXkZycjIMHD6Jfv34QCAT4+uuvcezYMezduxf79u3DM888g7fffhvHjh1rdZNuc5WCzEABiyM0N77Wxs39jl9++WUkJSUZvG9Lwbh79+4AgAsXLmD48OEWjVXX77//jokTJ2LEiBHYuHEjOnToABcXF2zevBnbt29vcn/d7I20TxTIiN1ERUXhwIEDqKio0MvKrl69yt8OADExMdBoNLh8+TL69u1r8LFiYmIAAEFBQUhMTGz1Z8fExOCll17CSy+9hMzMTPTt2xdvv/02tm7dyt9n8ODBGDx4MP71r39h+/btmDVrFnbs2KG3j8scUVFR0Gg0uHXrFrp06cJff/36dYse19Y6deoEAHBxcTHqd9zYhAkTkJyc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)
:::
:::::
::::::
::::::::
::::::::::::::::

:::::::::::::::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::::::::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::::::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[35\]:
:::

::::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
:::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    plt.figure(figsize=(5, 2.4))
    df_project['w'].plot(title='Job Weight Chart')
    plt.show()
:::
::::
:::::
:::::::
:::::::::

:::::::: jp-Cell-outputWrapper
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

:::::: {.jp-OutputArea .jp-Cell-outputArea}
::::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,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)
:::
:::::
::::::
::::::::
::::::::::::::::
