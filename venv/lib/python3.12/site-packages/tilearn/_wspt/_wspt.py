import tilearn as tl

def wspt(a):
    """
    Sort the list `a` using the WSPT algorithm.

    Parameters
    ----------
    a : list
        A list or an array containing the job table data that needs to be sorted.

    Returns
    -------
    list
        A matrix of size `job_amount(a) × 5`.
    """
    a = tl.factor_data(a)
    a.sort(key=lambda x: x[5], reverse=True)
    return a