def job_amount(a):
    return len(a)

def p_factor_nonprec(i, a):
    p_factor_nonprec = a[i][4]/a[i][1]
    return p_factor_nonprec

def p_factor_prec_tu(i, a):
    if i < 0:
        return 0
    return a[i][4] + p_factor_prec_tu(i-1,a,a[i][1])

def p_factor_prec(i, a, job_amount, job_scale, sum):
    return p_factor_prec_tu(i,a,a[i][1])/sum

def list_gen(rows, cols):
    a = [[0 for j in range(cols)] for i in range(rows)]
    return a

def calculate_factor(a, plan_time):
    list = list_gen(job_amount(a), 1)
    for i in range(job_amount(a)):
        list[i][0] = p_factor_nonprec(i, a)
    return list

def factor_data(a, plan_time):
    """
    Creates `p-factor` data for the job list `a`.

    Notes
    -----
    The `p-factor` pertains to the non-precedence job type in the `1||∑w_jC_j` problem.

    Parameters
    ----------
    a : list or array
        A list or an array that contains the job table data.
    plan_time : int
        The due date by which all jobs in the provided list need to be completed.

    Returns
    -------
    list or array
        A matrix of size `job_amount(a) × 6`.
    """
    for i in range(job_amount(a)):
        a[i].extend(calculate_factor(a, plan_time)[i])
    return a
