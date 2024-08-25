import tilearn as tl
import numpy as np

x = [[1, 2, 3, 6, 3],[2, 4, 8, 4, 2],[2, 4, 8, 6, 7]]
var = 5
maxm, maxn = 1000, 1000
a = [[0 for i in range(5)] for j in range(5)]

def non_pre(a, prec, plan_time):
     for i in range(tl.job_amount(a)):
          for j in range(var):
               print(a[i][j])

          if prec == 0:
               print(tl.process(
                    i, a, plan_time,
                    tl.jobscale(
                         a, tl.job_amount(a)
                         )
                    ),
                    tl.p_factor_nonprec(
                         i, a,
                         tl.process(
                              i, a, plan_time,
                              tl.jobscale(
                                   a, tl.job_amount(a)
                                   )
                              )
                         )
                    )
               
#non_pre(x, 0, 10)

#print(a)