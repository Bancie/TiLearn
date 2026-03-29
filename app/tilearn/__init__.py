"""Public API surface for the :mod:`tilearn` package.

The package exposes utility functions for single-machine scheduling workflows,
including:

- factor computation for dispatching rules,
- sorting by classic sequencing heuristics (WSPT and EDD),
- job-list orchestration across multiple CSV sources.

Notes
-----
This module re-exports many symbols via wildcard imports to provide a compact
entrypoint for scripts. The canonical implementations live in the following
submodules:

- :mod:`tilearn.bs.basis`
- :mod:`tilearn.wspt.wspt`
- :mod:`tilearn.edd.edd`
- :mod:`tilearn.data.data`
- :mod:`tilearn.joblist.plat`
- :mod:`tilearn.joblist.run`

Examples
--------
Import commonly used helpers from a single namespace:

>>> import tilearn as tl
>>> jobs = [
...     ["J1", 2.0, 0, 8, 4.0],
...     ["J2", 1.0, 0, 5, 1.0],
... ]
>>> tl.wspt(jobs)  # doctest: +NORMALIZE_WHITESPACE
[['J1', 2.0, 0, 8, 4.0, 2.0], ['J2', 1.0, 0, 5, 1.0, 1.0]]
"""

from tilearn.bs.basis import *
from tilearn.wspt.wspt import *
from tilearn.edd.edd import *
from tilearn.data import data
from tilearn.joblist import plat
from tilearn.joblist.run import *
