"""WSPT sequencing helper.

This module exposes a single convenience function that ranks jobs by decreasing
``w / p`` priority factor (Weighted Shortest Processing Time rule).
"""

import tilearn as tl


def wspt(a):
    """Sort jobs in-place by descending WSPT factor.

    Parameters
    ----------
    a : list[list[object]]
        Job table with at least five base columns ``[name, p, r, d, w]``.

    Returns
    -------
    list[list[object]]
        Same object as ``a`` after:

        1. appending factor column ``w / p`` at index ``5`` via
           :func:`tilearn.factor_data`,
        2. sorting rows in descending order of the appended factor.

    Raises
    ------
    ZeroDivisionError
        If any processing time ``p`` is zero.
    IndexError
        If a row has fewer than five columns.

    Notes
    -----
    - Mutation is in-place and cumulative; calling this function multiple times
      on the same table can append additional factor columns.
    - Ties are resolved by Python's stable ``list.sort`` behavior, preserving
      relative order of equal-factor rows.

    Examples
    --------
    >>> jobs = [
    ...     ["J1", 2.0, 0, 10, 4.0],
    ...     ["J2", 1.0, 0, 7, 1.0],
    ... ]
    >>> wspt(jobs)  # doctest: +NORMALIZE_WHITESPACE
    [['J1', 2.0, 0, 10, 4.0, 2.0], ['J2', 1.0, 0, 7, 1.0, 1.0]]
    """
    a = tl.factor_data(a)
    a.sort(key=lambda x: x[5], reverse=True)
    return a