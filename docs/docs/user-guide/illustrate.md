# End-to-End Illustrative Workflow

This guide shows a reproducible workflow for combining:

- independent job lists (`prec=0`), and
- precedence-style job lists (`prec=1`)

with `tilearn.optimal_list`.

## Project structure

```text
project/
├── run.py
└── data/
    ├── backup/
    ├── list1.csv
    ├── list2.csv
    └── list3.csv
```

The `backup/` directory is used as temporary working storage.

## CSV format

All lists use:

```csv
Name,p,r,d,w
```

Example:

```csv
Name,p,r,d,w
J1,4,0,100,0.65
J2,1,0,100,0.84
J3,3,0,100,0.46
```

## Runnable script

```python
import csv
import tilearn as tl
from tilearn import plat as pl

original = "data"
backup = "data/backup"

lists = [
    pl.List(backup_path=backup, file_path="data/list1.csv", prec=0),
    pl.List(backup_path=backup, file_path="data/list2.csv", prec=1),
    pl.List(backup_path=backup, file_path="data/list3.csv", prec=1),
]

schedule = tl.optimal_list(lists, original, backup)

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "p", "r", "d", "w", "factor"])
    writer.writerows(schedule)

print("Generated output.csv with", len(schedule), "rows")
```

Run:

```bash
pip install tilearn
python run.py
```

## Behavior notes

- `prec=0`: list is ranked with non-precedence factor (`w/p` behavior).
- `prec=1`: list is ranked with cumulative precedence-style factor
  (`sum(w)/sum(p)` along list order).
- `optimal_list` updates files inside `backup/` during processing and clears
  temporary CSV files at the end.

Use a dedicated backup folder for safe runs.

## Continue learning

- [WSPT guide](/user-guide/single-machine/completion/wspt)
- [EDD guide](/user-guide/single-machine/lateness/edd)
- [Joblist API](/api-reference/modules/joblist)
- [Data I/O API](/api-reference/modules/data-io)
