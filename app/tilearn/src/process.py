import tilearn

x = [[1, 2, 3, 6, 3],[2, 4, 8, 4, 2],[2, 4, 8, 6, 7],[2, 4, 8, 4, 2],[2, 4, 8, 4, 2]]
"""
var = 5
maxm, maxn = 1000, 1000
# a = [[0 for i in range(5)] for j in range(5)]
"""

def calculate(a, plan_time):
    list = tl.list_gen(tl.job_amount(a), 1)
    for i in range(tl.job_amount(a)):
        list[i][0] = tl.process(i, a, plan_time,tl.jobscale(a, tl.job_amount(a)))
    return list

def process_data(a, plan_time):
    for i in range(tl.job_amount(a)):
        a[i].extend(calculate(a, plan_time)[i])
    return a

print(process_data(x, 3))