import tilearn as tl
from tilearn import _plat as pl

original_path = '/Users/chibangnguyen/Documents/TiLearn/tests/personal-list'
backup_path = '/Users/chibangnguyen/Documents/TiLearn/tests/personal-list/backup'
list1 = '/Users/chibangnguyen/Documents/TiLearn/tests/personal-list/GTH-GTH.csv'
list2 = '/Users/chibangnguyen/Documents/TiLearn/tests/personal-list/DSA-DSA.csv'
list3 = '/Users/chibangnguyen/Documents/TiLearn/tests/personal-list/Tieng Anh-Tieng Anh.csv'

lists = [
    pl.List(file_path=list1, prec=1),
    pl.List(file_path=list2, prec=1),
    pl.List(file_path=list3, prec=1)
]

for row in tl.optimal_list(lists, original_path, backup_path):
    print(row)