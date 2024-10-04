import tilearn as tl
from tilearn import _plat as pl

tests = '/Users/chibangnguyen/Documents/TiLearn/app/tests'
backup = '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup'

lists = [
    pl.List(backup, file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/folder/folderx/data.csv', prec=0),
    pl.List(backup, file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/folder2/data2.csv', prec=0),
    pl.List(backup, file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/data3.csv', prec=0)
]

for row in tl.optimal_list(lists, tests, backup):
    print(row)