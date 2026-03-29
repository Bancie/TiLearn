"""Cross-file scheduling runner utilities.

This module coordinates iterative extraction of the next selected jobs across
multiple CSV-backed lists. It combines helper APIs from ``tilearn.joblist.plat``
and ``tilearn.data.data`` to maintain temporary files while building a final
ordered sequence.
"""

import tilearn as tl
from tilearn import data
from tilearn import plat as pl


def set_prec(lists, op, row):
    """Create a block of selected rows for precedence mode output.

    Parameters
    ----------
    lists : list
        Unused compatibility argument retained by current API signature.
    op : list[list[object]]
        Candidate ranked rows from a selected source list.
    row : int
        Number of rows from the beginning of ``op`` to copy.

    Returns
    -------
    list[list[object]]
        New matrix with shape ``(row, 6)`` copied from the first ``row`` rows of
        ``op``.

    Notes
    -----
    In precedence mode, the algorithm may append a prefix of rows at once.

    Examples
    --------
    >>> ranked = [["J1", 2.0, 0, 8, 4.0, 2.0], ["J2", 1.0, 0, 5, 1.0, 1.0]]
    >>> set_prec([], ranked, 1)
    [['J1', 2.0, 0, 8, 4.0, 2.0]]
    """
    set = tl.list_gen(row, 6)
    for i in range(len(set)):
        for j in range(len(set[i])):
            if i == 0 and j == 0:
                set[i][j] = str(op[i][j])
            set[i][j] = op[i][j]
    return set


def set(lists, op, row):
    """Create a one-row selection block for non-precedence mode.

    Parameters
    ----------
    lists : list
        Unused compatibility argument retained by current API signature.
    op : list[list[object]]
        Candidate ranked rows from a selected source list.
    row : int
        Index of row in ``op`` to copy.

    Returns
    -------
    list[list[object]]
        Single-row matrix of shape ``(1, 6)`` containing the selected row.

    Examples
    --------
    >>> ranked = [["J1", 2.0, 0, 8, 4.0, 2.0], ["J2", 1.0, 0, 5, 1.0, 1.0]]
    >>> set([], ranked, 1)
    [['J2', 1.0, 0, 5, 1.0, 1.0]]
    """
    set = tl.list_gen(1, 6)
    fix_row = row
    for i in range(len(set)):
        for j in range(len(set[i])):
            if i == 0 and j == 0:
                set[i][j] = str(op[fix_row][j])
            set[i][j] = op[fix_row][j]
    return set


def set_const(lists, prec, op, row):
    """Dispatch row-copy behavior by precedence mode.

    Parameters
    ----------
    lists : list
        Compatibility argument forwarded to helper functions.
    prec : int
        Mode selector: ``1`` calls :func:`set_prec`, ``0`` calls :func:`set`.
    op : list[list[object]]
        Candidate ranked rows.
    row : int
        Row count/index interpreted by selected helper.

    Returns
    -------
    list[list[object]] or None
        Copied selection block. Returns ``None`` for unsupported ``prec``.

    Examples
    --------
    >>> ranked = [["J1", 2.0, 0, 8, 4.0, 2.0]]
    >>> set_const([], 0, ranked, 0)
    [['J1', 2.0, 0, 8, 4.0, 2.0]]
    """
    if prec == 1:
        return set_prec(lists, op, row)
    elif prec == 0:
        return set(lists, op, row)


def file_seek(lists, path):
    """Count how many list objects still contain at least one job row.

    Parameters
    ----------
    lists : list
        Collection of list-like objects exposing an ``info()`` method.
    path : str or os.PathLike
        Directory used as baseline for CSV file count.

    Returns
    -------
    int
        Number of non-empty list sources.

    Examples
    --------
    >>> # active_sources = file_seek(list_objects, "tmp_backup")  # doctest: +SKIP
    """
    sum = pl.count_file(path)
    for sublist in lists:
        if sublist.info() == []:
            sum -= 1
    return sum


def optimal_list(lists, path, backup_path):
    """Build a global sequence by repeatedly selecting best available jobs.

    Parameters
    ----------
    lists : list[pl.List]
        Collection of per-file list descriptors.
    path : str or os.PathLike
        Source directory containing original CSV files.
    backup_path : str or os.PathLike
        Temporary working directory where source CSV files are copied and
        destructively updated during iteration.

    Returns
    -------
    list[list[object]]
        Final ordered sequence assembled from all lists. Each output row
        contains six columns (base job columns plus one factor column).

    Raises
    ------
    OSError
        Propagated from backup/read/write/delete filesystem operations.
    IndexError
        If list/rank indexing becomes inconsistent with file contents.

    Notes
    -----
    Workflow summary:

    1. Copy CSV files from ``path`` to ``backup_path``.
    2. Repeatedly locate globally best candidate using
       :func:`tilearn.joblist.plat.location`.
    3. Append selected row(s) to output, then rewrite the corresponding working
       CSV using :func:`tilearn.data.updated`.
    4. Remove all temporary CSV files with :func:`tilearn.data.clear`.

    This function performs heavy filesystem side effects in ``backup_path`` and
    should be run with a dedicated temporary directory.

    Examples
    --------
    >>> # lists = [pl.List("tmp_backup", "source/a.csv", 0)]
    >>> # final_jobs = optimal_list(lists, "source", "tmp_backup")  # doctest: +SKIP
    """
    set_j = []
    data.backup(path, backup_path)
    jc = pl.ja_all(lists, path)
    while jc > 0:
        opt_list = lists[pl.location(lists, type="sub")].run()
        row_list = pl.location(lists, type="row")
        opt_file = lists[pl.location(lists, type="sub")].path
        check = lists[pl.location(lists, type="sub")].check()
        if check == 1:
            if file_seek(lists, path=backup_path) == 1:
                set_j.extend(opt_list)
                break
            set_j.extend(set_const(lists, prec=1, op=opt_list, row=row_list + 1))
            data.updated(opt_file, prec=1, opt_row=row_list)
            jc -= row_list + 1
        elif check == 0:
            set_j.extend(set_const(lists, prec=0, op=opt_list, row=row_list))
            data.updated(opt_file, prec=0, opt_row=row_list)
            jc -= 1
    data.clear(backup_path)
    return set_j