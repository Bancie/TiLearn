import tilearn as tl
from tilearn import _plat as pl

tests = '/Users/chibangnguyen/Documents/TiLearn/app/tests'
backup = '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup'

lists = [
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/folder1/data.csv', prec=0),
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/folder1/data2.csv', prec=1),
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/folder1/data3.csv', prec=0)
]

for row in tl.optimal_list(lists, tests, backup):
    print(row)