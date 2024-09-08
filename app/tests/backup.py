import tilearn as tl
from tilearn import _data as data
from tilearn import _plat as pl
import os
import csv
import shutil
import glob

# print(data.path('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'))
# print(data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'))
data.backup('/Users/chibangnguyen/Documents/TiLearn/app/tests', '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup')

lists = [
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv', prec=0),
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv', prec=0),
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/data3.csv', prec=0)
]

# print(pl.location(lists, type='sub'))

for row in tl.optimal_list(lists, '/Users/chibangnguyen/Documents/TiLearn/app/tests', '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup'):
    print(row)

# row_list = pl.location(lists, type='row')
# opt_file = lists[pl.location(lists, type='sub')].path

# print(row_list, opt_file)
# print(data.prec(opt_file, row_list))
# rows = data.none(opt_file, row_list)
# print(rows)

# data.updated(opt_file, prec=1, opt_row=row_list)
# data.clear('/Users/chibangnguyen/Documents/TiLearn/app/tests/backup')

# print(tl.set_const(lists, prec=1))


# data.clear('/Users/chibangnguyen/Documents/TiLearn/app/tests/backup')

# for row in tl.optimal_list(lists,'/Users/chibangnguyen/Documents/TiLearn/app/tests', '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup'):  
#     print(row)

# data.updated('/Users/chibangnguyen/Documents/TiLearn/app/tests/backup/data.csv', prec=1, opt_row=1)

# print(pl.ja_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))
# print(tl.set_const(lists, prec=1))

# for sublist in lists:
#     print(sublist.path())
# print(lists[1].path)

# for sublist in lists:
#     print(sublist.path)
