import tilearn as tl
from tilearn import _data as data
from tilearn import _plat as pl

# print(data.path('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'))
# print(data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'))
# data.backup('/Users/chibangnguyen/Documents/TiLearn/app/tests', '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup')
# data.clear('/Users/chibangnguyen/Documents/TiLearn/app/tests/backup')

lists = [
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'), prec=1),
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv'), prec=1),
    pl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data3.csv'), prec=1)
]

print(pl.ja_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

# for sublist in lists:
#     for row in sublist.run():
#         print(row)
