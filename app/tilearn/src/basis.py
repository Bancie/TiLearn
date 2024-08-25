var = 5
maxm, maxn = 1000, 1000
# a = [[0 for i in range(maxm)] for j in range(maxn)]

def job_amount(a):
    return len(a)

def jobscale(a, job_amount):
    sum = 0
    for i in range(job_amount):
        for j in range(1):
            sum += a[i][1]
    return sum

def process(i, a, plan_time, job_scale):
    p = (a[i][1] * plan_time)/job_scale
    return p

def p_factor_nonprec(i, a, p):
    p_factor_nonprec = a[i][4]/p
    return p_factor_nonprec

def p_factor_prec_tu(i, a, p):
    if i < 0:
        return 0
    return a[i][4] + p_factor_prec_tu(i-1,a,p)

def p_factor_prec(i, a, job_amount, job_scale, p, sum):
    return p_factor_prec_tu(i,a,p)/sum

def list_gen(rows, cols):
    a = [[0 for j in range(cols)] for i in range(rows)]
    return a


"""
x = [[1, 2, 3],
     [2, 4, 8], 
     [1, 2, 3],
     [2, 4, 8]]

print(list_gen(5, 3))
"""