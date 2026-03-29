"""Object and helpers for per-file job-list orchestration.

This module defines:

- :class:`List`: a lightweight object describing one backed-up CSV list,
- helper functions that aggregate multiple :class:`List` objects and locate the
  current globally optimal row.
"""

import os

import tilearn as tl
from tilearn import data


class List:
    """Represent one scheduling list bound to a backed-up CSV file.

    Parameters
    ----------
    backup_path : str or os.PathLike
        Directory containing the working copy of CSV files.
    file_path : str or os.PathLike
        Path to original CSV file. Only its basename is used to derive the
        backed-up file path.
    prec : int
        Scheduling mode flag:

        - ``1`` for precedence-aware ratio mode (uses :func:`tilearn.sum_factor`)
        - ``0`` for non-precedence ratio mode (uses :func:`tilearn.factor_data`)

    Attributes
    ----------
    backup : str
        Absolute path to backup directory.
    path : str
        Absolute path to backed-up CSV file corresponding to this list.
    prec : int
        Stored precedence flag.

    Notes
    -----
    The object reads CSV data from disk whenever :meth:`info` or :meth:`run` is
    called. It does not cache loaded rows.
    """

    def __init__(self, backup_path, file_path, prec):
        """Initialize a list descriptor from paths and mode."""
        self.backup = os.path.abspath(backup_path)
        self.path = data.path(os.path.abspath(file_path), self.backup)
        self.prec = prec

    def info(self):
        """Load raw typed rows from this list's CSV file.

        Returns
        -------
        list[list[object]]
            Parsed rows as returned by :func:`tilearn.data.read_file`.

        Examples
        --------
        >>> # jobs = my_list.info()  # doctest: +SKIP
        """
        return data.read_file(self.path)

    def check(self):
        """Return stored precedence mode for this list.

        Returns
        -------
        int
            ``1`` for precedence mode, ``0`` for non-precedence mode.
        """
        return self.prec

    def path(self):
        """Return the backing CSV path string.

        Returns
        -------
        str
            Path to the working CSV file.
        """
        return self.path

    def run(self):
        """Compute per-row priority factors for this list.

        Returns
        -------
        list[list[object]]
            Freshly loaded rows with one appended factor column:

            - cumulative ``sum(w)/sum(p)`` when ``prec == 1``
            - direct ``w/p`` when ``prec == 0``

        Notes
        -----
        The returned table is derived from newly loaded CSV data each call.

        Examples
        --------
        >>> # ranked_rows = my_list.run()  # doctest: +SKIP
        """
        if self.prec == 1:
            return tl.sum_factor(data.read_file(self.path))
        elif self.prec == 0:
            return tl.factor_data(data.read_file(self.path))


def count_file(folder_path):
    """Count top-level CSV files in a directory.

    Parameters
    ----------
    folder_path : str or os.PathLike
        Directory to inspect.

    Returns
    -------
    int
        Number of files ending with ``.csv`` directly under ``folder_path``.

    Examples
    --------
    >>> # count_file("tmp_backup")  # doctest: +SKIP
    """
    csv_count = len([file for file in os.listdir(folder_path) if file.endswith(".csv")])
    return csv_count


def ja_all(lists, path):
    """Compute total job count across all active CSV lists.

    Parameters
    ----------
    lists : list[List]
        Collection of :class:`List` objects.
    path : str or os.PathLike
        Directory used to determine how many CSV-backed lists are considered.

    Returns
    -------
    int
        Total number of jobs across the first ``count_file(path)`` list objects.

    Notes
    -----
    This function assumes that ``len(lists)`` is at least ``count_file(path)``.

    Examples
    --------
    >>> # total_jobs = ja_all(list_objects, "tmp_backup")  # doctest: +SKIP
    """
    sum = 0
    folder_path = path
    csv_count = len([file for file in os.listdir(folder_path) if file.endswith(".csv")])
    for i in range(csv_count):
        count = sum + tl.job_amount(lists[i].info())
        sum = count
    return count


def location(lists, type):
    """Locate list index or row index of the current maximum factor.

    Parameters
    ----------
    lists : list[List]
        Collection of :class:`List` objects.
    type : {'sub', 'row'}
        Selector for output:

        - ``'sub'`` returns index of list containing the best candidate row
        - ``'row'`` returns row index within that selected list

    Returns
    -------
    int
        Index selected according to ``type``.

    Notes
    -----
    The ranking value is read from column index ``5`` in each list produced by
    :meth:`List.run`.

    Examples
    --------
    >>> # best_list_idx = location(list_objects, "sub")  # doctest: +SKIP
    >>> # best_row_idx = location(list_objects, "row")   # doctest: +SKIP
    """
    opt = tl.list_gen(2, 1)
    max_value = 0
    init = 0
    for sublist in lists:
        for i in range(tl.job_amount(sublist.info())):
            if sublist.run()[i][5] > max_value:
                max_value = sublist.run()[i][5]
                opt[0] = init
                opt[1] = i
        init += 1
    if type == "sub":
        return opt[0]
    elif type == "row":
        return opt[1]