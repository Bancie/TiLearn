import tilearn as tl

x = [[1, 2, 3, 6, 3],[2, 4, 8, 4, 2],[2, 4, 8, 6, 7],[2, 4, 8, 4, 2],[2, 4, 8, 4, 2]]

def calculate(a, plan_time):
    list = tl.list_gen(tl.job_amount(a), 1)
    for i in range(tl.job_amount(a)):
        list[i][0] = tl.p_factor_nonprec(i, a,tl.process(i, a, plan_time,tl.jobscale(a, tl.job_amount(a))))
    return list

def total_completion_time(a, plan_time):
    result = tl.process_data(a, plan_time)
    for i in range(tl.job_amount(a)):
        result[i].extend(calculate(a, plan_time)[i])
    return result