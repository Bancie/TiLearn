import tilearn as tl
from tilearn import _plat as pl

lists = [
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv', prec=1),
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv', prec=1),
]

for row in tl.optimal_list(lists, '/Users/chibangnguyen/Documents/TiLearn/app/tests', '/Users/chibangnguyen/Documents/TiLearn/app/tests/backup'):
    print(row)