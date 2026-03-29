---
title: Getting started
description: Install tilearn, understand the data model, and run your first scheduling example.
---

`tilearn` is a Python library for single-machine scheduling workflows, including:

- weighted completion-time ranking (WSPT),
- due-date-first ranking (EDD),
- mixed multi-list orchestration with optional precedence mode.

## Install

```bash
pip install tilearn
```

Verify installation:

```bash
python -c "import tilearn; print('tilearn imported successfully')"
```

## First run

```python
import tilearn as tl

jobs = [
    ["J1", 2.0, 0, 8, 4.0],
    ["J2", 1.0, 0, 5, 1.0],
    ["J3", 3.0, 0, 6, 6.0],
]

print("WSPT:")
for row in tl.wspt([r[:] for r in jobs]):
    print(row)

print("\nEDD:")
for row in tl.edd([r[:] for r in jobs]):
    print(row)
```

## Data format

Most APIs expect rows in this order:

```python
[name, p, r, d, w]
```

- `name`: job identifier (`str`)
- `p`: processing time
- `r`: release time
- `d`: due date
- `w`: weight

Many helper functions append computed columns (for example `w/p`, completion
time, lateness) directly to each row.

## Problem notation

TiLearn follows standard scheduling notation:

$$
\alpha \mid \beta \mid \gamma
$$

- `\alpha`: machine environment (`1` for single machine),
- `\beta`: constraints (for example `prec`, `r_j`),
- `\gamma`: objective (for example `L_{\max}`, `\sum w_j C_j`).

## Where to go next

- [User Guide](/user-guide): theory + practical workflows.
- [API reference](/api-reference): function-level contracts.
- [Building from source](/building-from-source): contributor setup.
