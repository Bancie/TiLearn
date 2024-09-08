import tilearn as tl
from tilearn import _data as data
from tilearn import _plat as pl

# print(data.path('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'))
# print(data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'))
data.backup('/Users/chibangnguyen/Documents/TiLearn/app/tests', '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup')

lists = [
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'), prec=0),
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv'), prec=0),
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data3.csv'), prec=0)
]

# print(pl.ja_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))
print(tl.set_const(lists, prec=1))

# for sublist in lists:
#     for row in sublist.run():
#         print(row)

data.clear('/Users/chibangnguyen/Documents/TiLearn/app/tests/backup')