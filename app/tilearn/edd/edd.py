"""EDD sequencing helper.

This module implements Earliest Due Date ordering for a job table.
"""


def edd(a):
    """Sort jobs in-place by ascending due date.

    Parameters
    ----------
    a : list[list[object]]
        Job table where due date ``d`` is stored at column index ``3``.

    Returns
    -------
    list[list[object]]
        Same object as ``a`` sorted in non-decreasing due-date order.

    Raises
    ------
    IndexError
        If a row has fewer than four columns.
    TypeError
        If due-date values are not mutually comparable.

    Notes
    -----
    EDD is a classic dispatching rule commonly used to reduce maximum lateness
    in single-machine deterministic scheduling.

    Examples
    --------
    >>> jobs = [
    ...     ["J1", 2.0, 0, 9, 4.0],
    ...     ["J2", 1.0, 0, 4, 1.0],
    ... ]
    >>> edd(jobs)
    [['J2', 1.0, 0, 4, 1.0], ['J1', 2.0, 0, 9, 4.0]]
    """
    a.sort(key=lambda x: x[3], reverse=False)
    return a