import tilearn as tl
from tilearn import data

lists = [
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'), prec=1),
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv'), prec=1)
]

print(tl.opt_loca(lists))

# print(tl.job_amount_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

# for sublist in lists:
#     print(sublist.run())
# print(mixed('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))
# print(lists[1].run())
# print(tl.list_gen(job_amount_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists), 6))