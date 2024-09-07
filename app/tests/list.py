import tilearn as tl
import numpy as np
from tilearn import data

lists = [
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'), prec=1),
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv'), prec=1),
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data3.csv'), prec=1)
]

# opt_list = lists[tl.opt_loca(lists, pick='sub')].run()
# row_list = tl.opt_loca(lists, pick='row')
# opt_list = np.delete(opt_list, row_list, axis=0)
# print(opt_list)

# for sublist in lists:
#     for row in sublist.run():
#         print(row)

# print('\n')

# for row in tl.set_construct(lists, 0):
#     print(row)

# print(tl.set_const(lists, 1))
# print(tl.opt_loca(lists, pick='sub'))
# print(tl.ja_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

# print(tl.main_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

# print(tl.optimal_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

for row in tl.optimal_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists):
    print(row)