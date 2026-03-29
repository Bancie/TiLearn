"""CSV file management utilities for :mod:`tilearn`.

This module centralizes disk I/O used by multi-file scheduling workflows:

- backup source CSV files into a temporary workspace,
- load typed job data from CSV into in-memory lists,
- update CSV files after selecting jobs,
- clear temporary CSV artifacts.

All functions expect CSV files with the canonical five-column header:
``Name,p,r,d,w``.
"""

import csv
import glob
import os
import shutil


def backup(src, dist):
    """Copy all CSV files from ``src`` tree into ``dist`` directory.

    Parameters
    ----------
    src : str or os.PathLike
        Root directory scanned recursively for ``*.csv`` files.
    dist : str or os.PathLike
        Destination directory where discovered files are copied.

    Returns
    -------
    None
        This function performs file-system side effects only.

    Raises
    ------
    FileNotFoundError
        If ``src`` or ``dist`` does not exist.
    PermissionError
        If the process lacks read/write permissions.
    shutil.SameFileError
        If source and destination resolve to the same path.

    Notes
    -----
    The destination structure is flattened by ``shutil.copy`` semantics used in
    a loop. If multiple files share the same basename, later copies may
    overwrite earlier ones.

    Examples
    --------
    >>> # backup("datasets", "tmp_backup")
    >>> # Copies every CSV found under datasets/** into tmp_backup.
    """
    csv_files = glob.glob(os.path.join(src, "**", "*.csv"), recursive=True)
    for file in csv_files:
        shutil.copy(file, dist)


def path(original_path, backup_path):
    """Build backup-file path preserving only source basename.

    Parameters
    ----------
    original_path : str or os.PathLike
        Original CSV absolute or relative path.
    backup_path : str or os.PathLike
        Backup directory path.

    Returns
    -------
    str
        Full path computed as ``join(backup_path, basename(original_path))``.

    Examples
    --------
    >>> path("/data/source/jobs.csv", "/tmp/backup")
    '/tmp/backup/jobs.csv'
    """
    filename = os.path.basename(original_path)
    new_directory = os.path.join(backup_path, filename)
    return new_directory


def read_file(file_path):
    """Load a job CSV and coerce columns to project-specific types.

    Parameters
    ----------
    file_path : str or os.PathLike
        Path to a CSV file with columns ``Name,p,r,d,w``.

    Returns
    -------
    list[list[object]]
        Parsed job rows with per-column typing:

        - column ``0`` (Name) -> ``str``
        - columns ``1`` and ``4`` (p, w) -> ``float``
        - columns ``2`` and ``3`` (r, d) -> ``int``

    Raises
    ------
    FileNotFoundError
        If ``file_path`` does not exist.
    ValueError
        If a numeric field cannot be converted to expected numeric type.
    IndexError
        If a row contains fewer than five fields.

    Examples
    --------
    >>> # Suppose jobs.csv contains:
    >>> # Name,p,r,d,w
    >>> # J1,2,0,6,3
    >>> read_file("jobs.csv")
    [['J1', 2.0, 0, 6, 3.0]]
    """
    data = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for i in range(0, 5):
                if i == 0:
                    row[i] = str(row[i])
                elif i == 1 or i == 4:
                    row[i] = float(row[i])
                else:
                    row[i] = int(row[i])
            data.append(row)
    return data


def precedence(file_path, opt_row):
    """Return remaining rows after removing selected prefix in precedence mode.

    Parameters
    ----------
    file_path : str or os.PathLike
        CSV file to read.
    opt_row : int
        Zero-based selected row index. Rows with index ``<= opt_row`` are
        discarded; rows with index ``> opt_row`` are kept.

    Returns
    -------
    list[list[object]]
        Processed rows converted to project data types.

    Raises
    ------
    FileNotFoundError
        If ``file_path`` is invalid.
    ValueError
        If ``opt_row`` or numeric fields cannot be converted.

    Notes
    -----
    This helper is used by :func:`updated` when precedence-aware extraction is
    enabled (``prec == 1``).

    Examples
    --------
    >>> # Given rows A, B, C and opt_row=1, only C is returned.
    >>> precedence("jobs.csv", 1)  # doctest: +SKIP
    """
    with open(file_path, "r") as infile:
        reader = csv.reader(infile)
        next(reader)
        rows = []
        for index, row in enumerate(reader):
            if index > int(opt_row):
                processed_row = [str(row[0])] + [float(row[1])] + [
                    int(val) if idx != 4 else float(val)
                    for idx, val in enumerate(row[2:], start=2)
                ]
                rows.append(processed_row)
    return rows


def none(file_path, opt_row):
    """Return rows after removing exactly one selected row.

    Parameters
    ----------
    file_path : str or os.PathLike
        CSV file to read.
    opt_row : int
        Zero-based selected row index to remove.

    Returns
    -------
    list[list[object]]
        All rows except ``opt_row``, with project-specific type coercion.

    Raises
    ------
    FileNotFoundError
        If ``file_path`` does not exist.
    ValueError
        If ``opt_row`` or numeric values are invalid.

    Examples
    --------
    >>> # Given rows A, B, C and opt_row=1, rows A and C are returned.
    >>> none("jobs.csv", 1)  # doctest: +SKIP
    """
    with open(file_path, "r") as infile:
        reader = csv.reader(infile)
        next(reader)
        rows = []
        for index, row in enumerate(reader):
            if index != int(opt_row):
                processed_row = [str(row[0])] + [float(row[1])] + [
                    int(val) if idx != 4 else float(val)
                    for idx, val in enumerate(row[2:], start=2)
                ]
                rows.append(processed_row)
    return rows


def updated(file_path, prec, opt_row):
    """Rewrite a job CSV after extracting selected jobs.

    Parameters
    ----------
    file_path : str or os.PathLike
        Target CSV file rewritten in-place.
    prec : int
        Mode selector:

        - ``1``: precedence mode, remove prefix via :func:`precedence`
        - ``0``: non-precedence mode, remove one row via :func:`none`
    opt_row : int
        Selected row index interpreted according to ``prec`` mode.

    Returns
    -------
    None
        This function rewrites ``file_path`` and does not return a value.

    Raises
    ------
    OSError
        If the file cannot be read or written.
    ValueError
        If mode/index conversions fail.

    Notes
    -----
    Output header is always reset to ``['Name', 'p', 'r', 'd', 'w']``.

    Examples
    --------
    >>> # Remove one selected row in non-precedence mode.
    >>> updated("jobs.csv", prec=0, opt_row=2)  # doctest: +SKIP
    """
    header = ["Name", "p", "r", "d", "w"]
    rows = []
    if prec == 1:
        rows = precedence(file_path, opt_row)
    elif prec == 0:
        rows = none(file_path, opt_row)
    with open(file_path, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(rows)


def clear(folder_path):
    """Delete all top-level CSV files in a directory.

    Parameters
    ----------
    folder_path : str or os.PathLike
        Directory containing temporary CSV files to remove.

    Returns
    -------
    None
        Files are removed from disk; no in-memory value is returned.

    Raises
    ------
    FileNotFoundError
        If a matched file disappears before deletion.
    PermissionError
        If the process cannot delete one or more files.

    Notes
    -----
    This function is intentionally non-recursive and only removes files
    matching ``folder_path/*.csv``.

    Examples
    --------
    >>> # clear("tmp_backup")
    >>> # Removes all CSV files directly inside tmp_backup.
    """
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    for file in csv_files:
        os.remove(file)

