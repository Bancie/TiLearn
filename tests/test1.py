import tilearn as tl
from tilearn import _plat as pl

original_path = '/Users/chibangnguyen/Documents/TiLearn/tests'
backup_path = '/Users/chibangnguyen/Documents/TiLearn/tests/backup'
list1 = '/Users/chibangnguyen/Documents/TiLearn/tests/GTH-GTH.csv'
list2 = '/Users/chibangnguyen/Documents/TiLearn/tests/DSA-DSA.csv'
list3 = '/Users/chibangnguyen/Documents/TiLearn/tests/Tieng Anh-Tieng Anh.csv'

lists = [
    pl.List(file_path=list1, prec=1),
    pl.List(file_path=list2, prec=0),
    pl.List(file_path=list3, prec=0)
]

for row in tl.optimal_list(lists, original_path, backup_path):
    print(row)