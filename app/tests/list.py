import tilearn as tl
from tilearn import _data as data
from tilearn import _plat as pl

lists = [
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'), prec=1),
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv'), prec=1),
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data3.csv'), prec=1)
]

# 2D list example
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# del matrix[0:1]

# print(matrix)


# print(pl.location(lists, type='row'))

# print(tl.optimal_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

# opt_list = lists[pl.location(lists, type='sub')].run()
# print(opt_list[2])
# print(tl.set(lists))

# set_j = []
# opt_list = lists[pl.location(lists, type='sub')].run()
# row_list = pl.location(lists, type='row')

# print(tl.set_non(lists))

# print(tl.updated(lists, set_j, opt_list, row_list))

# for row in tl.updated(lists, set_j, opt_list, row_list):
#     print(row)

# print(tl.optimal_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

for row in tl.optimal_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists):  
    print(row)
# print(lists[0].info())


# print(tl.set_const(lists, prec=0))
# print(tl.set_non(lists))
# print(tl.set_prec(lists))
# print(tl.set_const(lists, prec=0))

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
# print(tl.ja_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

# print(tl.main_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

