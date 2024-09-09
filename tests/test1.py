import tilearn as tl
from tilearn import _plat as pl

lists = [
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/tests/data.csv', prec=0),
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/tests/data2.csv', prec=1),
    pl.List(file_path='/Users/chibangnguyen/Documents/TiLearn/tests/data3.csv', prec=1)
]

for row in tl.optimal_list(lists, '/Users/chibangnguyen/Documents/TiLearn/tests', '/Users/chibangnguyen/Documents/TiLearn/tests/backup'):
    print(row)