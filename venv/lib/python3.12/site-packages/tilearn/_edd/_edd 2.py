import tilearn as tl

def edd(a):
    """
    Sort the list `a` using the EDD algorithm.

    Parameters
    ----------
    a : list
        A list or an array containing the job table data that needs to be sorted.

    Returns
    -------
    list
        A matrix of size `job_amount(a) × 5`.
    """
    a.sort(key=lambda x: x[3], reverse=False)
    return a