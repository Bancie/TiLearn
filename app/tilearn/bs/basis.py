"""Core scheduling utilities and feature-engineering helpers.

This module provides low-level operations over the internal job-table
representation used across :mod:`tilearn`.

A job row is typically represented as::

    [name, p, r, d, w, ...]

where:

- ``name`` is a job identifier (string),
- ``p`` is processing time,
- ``r`` is release time,
- ``d`` is due date,
- ``w`` is job weight.

Most functions in this module mutate input rows in-place by appending derived
columns (for example ``w / p`` factor, completion time, or lateness).
"""


def list_gen(rows, cols):
    """Create a 2D zero-initialized list.

    Parameters
    ----------
    rows : int
        Number of rows to allocate.
    cols : int
        Number of columns to allocate in each row.

    Returns
    -------
    list[list[int]]
        Matrix with shape ``(rows, cols)`` filled with ``0``.

    Notes
    -----
    This helper is used instead of ``numpy.zeros`` to keep dependencies
    minimal and preserve pure-Python list semantics.

    Examples
    --------
    >>> list_gen(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    a = [[0 for j in range(cols)] for i in range(rows)]
    return a


def job_amount(a):
    """Return the number of jobs contained in a table.

    Parameters
    ----------
    a : list[list[object]]
        Job table where each element is a job row.

    Returns
    -------
    int
        Total number of jobs.

    Examples
    --------
    >>> job_amount([["J1", 2.0, 0, 5, 1.0], ["J2", 1.0, 0, 2, 3.0]])
    2
    """
    return len(a)


def p_factor_nonprec(i, a):
    """Compute the non-precedence priority factor for one job.

    The priority factor is computed as ``w / p`` where ``w`` is job weight
    (column index ``4``) and ``p`` is processing time (column index ``1``).

    Parameters
    ----------
    i : int
        Row index of the target job in ``a``.
    a : list[list[object]]
        Job table with at least five columns per row.

    Returns
    -------
    float
        Priority factor for row ``i``.

    Raises
    ------
    IndexError
        If ``i`` is out of bounds or the row has insufficient columns.
    ZeroDivisionError
        If processing time ``p`` equals zero.

    Notes
    -----
    This metric is used by the WSPT-like ranking logic in this project.

    Examples
    --------
    >>> jobs = [["J1", 2.0, 0, 8, 6.0]]
    >>> p_factor_nonprec(0, jobs)
    3.0
    """
    p_factor_nonprec = a[i][4] / a[i][1]
    return p_factor_nonprec


def p_factor_prec_tu(i, a):
    """Recursively accumulate weighted value for precedence experiments.

    Parameters
    ----------
    i : int
        Current row index in the recursive traversal.
    a : list[list[object]]
        Job table with weight data at column index ``4``.

    Returns
    -------
    float or int
        Recursive accumulation value. Returns ``0`` when ``i < 0``.

    Notes
    -----
    This function reflects the current implementation and is kept for
    compatibility with existing code paths. It is not used by the default
    non-precedence scheduling flow.

    Examples
    --------
    >>> p_factor_prec_tu(-1, [["J1", 2.0, 0, 8, 6.0]])
    0
    """
    if i < 0:
        return 0
    return a[i][4] + p_factor_prec_tu(i - 1, a, a[i][1])


def p_factor_prec(i, a, job_amount, job_scale, sum):
    """Compute precedence-based factor normalized by cumulative sum.

    Parameters
    ----------
    i : int
        Target row index.
    a : list[list[object]]
        Job table.
    job_amount : int
        Compatibility argument retained by current API.
    job_scale : int or float
        Compatibility argument retained by current API.
    sum : int or float
        Divisor used for normalization.

    Returns
    -------
    float
        Normalized precedence factor for row ``i`` when helper calls are
        compatible.

    Raises
    ------
    TypeError
        In the current code path, this function delegates to
        :func:`p_factor_prec_tu` with an extra argument, which can trigger a
        signature mismatch.

    Notes
    -----
    Some parameters are currently unused in implementation but retained in the
    signature for backward compatibility.

    Examples
    --------
    >>> jobs = [["J1", 2.0, 0, 8, 6.0]]
    >>> p_factor_prec(0, jobs, 1, 1, 2.0)  # doctest: +SKIP
    """
    return p_factor_prec_tu(i, a, a[i][1]) / sum


def calculate_factor(a):
    """Compute ``w / p`` factors for all jobs without mutating ``a``.

    Parameters
    ----------
    a : list[list[object]]
        Job table where each row contains ``p`` at index ``1`` and ``w`` at
        index ``4``.

    Returns
    -------
    list[list[float]]
        Single-column matrix of shape ``(len(a), 1)`` where each row stores the
        computed priority factor.

    Examples
    --------
    >>> jobs = [["J1", 2.0, 0, 8, 6.0], ["J2", 1.0, 0, 3, 2.0]]
    >>> calculate_factor(jobs)
    [[3.0], [2.0]]
    """
    list = list_gen(job_amount(a), 1)
    for i in range(job_amount(a)):
        list[i][0] = p_factor_nonprec(i, a)
    return list


def factor_data(a):
    """Append non-precedence priority factors to each job row.

    Parameters
    ----------
    a : list[list[object]]
        Job table with schema ``[name, p, r, d, w]`` or compatible.

    Returns
    -------
    list[list[object]]
        Same object as ``a`` after appending one column per row at index ``5``
        representing ``w / p``.

    Notes
    -----
    - Mutation is in-place: each row is extended using ``list.extend``.
    - If called repeatedly on the same table, additional factor columns are
      appended each time.

    Examples
    --------
    >>> jobs = [["J1", 2.0, 0, 8, 6.0], ["J2", 1.0, 0, 3, 2.0]]
    >>> factor_data(jobs)  # doctest: +NORMALIZE_WHITESPACE
    [['J1', 2.0, 0, 8, 6.0, 3.0], ['J2', 1.0, 0, 3, 2.0, 2.0]]
    """
    for i in range(job_amount(a)):
        a[i].extend(calculate_factor(a)[i])
    return a


def c_time(a):
    """Append completion time ``C_j`` for each row in current sequence order.

    Parameters
    ----------
    a : list[list[object]]
        Ordered job table where processing time ``p`` is stored at index ``1``.

    Returns
    -------
    list[list[object]]
        Same object as ``a`` after appending completion times as a new column.

    Notes
    -----
    Completion times are computed cumulatively from top to bottom using the
    current row order; no sorting is performed here.

    Examples
    --------
    >>> jobs = [["J1", 2.0, 0, 8, 6.0], ["J2", 1.0, 0, 3, 2.0]]
    >>> c_time(jobs)  # doctest: +NORMALIZE_WHITESPACE
    [['J1', 2.0, 0, 8, 6.0, 2.0], ['J2', 1.0, 0, 3, 2.0, 3.0]]
    """
    sum = 0
    list = list_gen(job_amount(a), 1)
    for i in range(job_amount(a)):
        list[i][0] = sum + a[i][1]
        sum = list[i][0]
    for i in range(job_amount(a)):
        a[i].extend(list[i])
    return a


def lateness(a):
    """Append lateness ``L_j = C_j - d_j`` to each row.

    Parameters
    ----------
    a : list[list[object]]
        Job table that already contains completion time ``C_j`` at index ``5``
        and due date ``d_j`` at index ``3``.

    Returns
    -------
    list[list[object]]
        Same object as ``a`` with a new column containing lateness values.

    Notes
    -----
    Call :func:`c_time` before this function when starting from a base
    ``[name, p, r, d, w]`` table.

    Examples
    --------
    >>> jobs = [["J1", 2.0, 0, 5, 1.0, 4.0]]
    >>> lateness(jobs)
    [['J1', 2.0, 0, 5, 1.0, 4.0, -1.0]]
    """
    list = list_gen(job_amount(a), 1)
    for i in range(job_amount(a)):
        list[i][0] = a[i][5] - a[i][3]
    for i in range(job_amount(a)):
        a[i].extend(list[i])
    return a


def sum_factor(a):
    """Append cumulative ``sum(w) / sum(p)`` factor for precedence flow.

    Parameters
    ----------
    a : list[list[object]]
        Ordered job table with processing time ``p`` at index ``1`` and weight
        ``w`` at index ``4``.

    Returns
    -------
    list[list[object]]
        Same object as ``a`` with one appended column per row containing the
        cumulative ratio:

        ``(w_1 + ... + w_j) / (p_1 + ... + p_j)``.

    Notes
    -----
    The output is sequence-dependent. Reordering rows changes computed values.

    Examples
    --------
    >>> jobs = [["J1", 2.0, 0, 8, 4.0], ["J2", 1.0, 0, 3, 2.0]]
    >>> sum_factor(jobs)  # doctest: +NORMALIZE_WHITESPACE
    [['J1', 2.0, 0, 8, 4.0, 2.0], ['J2', 1.0, 0, 3, 2.0, 2.0]]
    """
    list = list_gen(job_amount(a), 3)
    sum_p = 0
    sum_w = 0
    for i in range(job_amount(a)):
        list[i][0] = sum_p + a[i][1]
        sum_p = list[i][0]
    for i in range(job_amount(a)):
        list[i][1] = sum_w + a[i][4]
        sum_w = list[i][1]
    for i in range(job_amount(a)):
        list[i][2] = list[i][1] / list[i][0]
    for i in range(job_amount(a)):
        a[i].append(list[i][2])
    return a