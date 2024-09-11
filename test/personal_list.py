import tilearn as tl
from tilearn import _plat as pl
import csv

original = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list'
backup = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/backup'
list1 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/CTRR-Cấu trúc rời rạc.csv'
list2 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/GTH-GTH.csv'
list3 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/LIST-Discrete list.csv'
list4 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/Listening-Listening.csv'
list5 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/LTMM-Lý thuyết mật mã.csv'
list6 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/Map-Map listening.csv'
list7 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/NCKH-Nghiên cứu khoa học.csv'
list8 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/p2-Speaking p2.csv'
list9 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/Supporting-Supporting.csv'
list10 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/T F N-T F NG.csv'
list11 = '/Users/chibangnguyen/Documents/TiLearn/test/Personal_list/Task 1-Task 1.csv'

lists = [
    pl.List(file_path=list1, prec=1),
    pl.List(file_path=list2, prec=1),
    pl.List(file_path=list3, prec=0),
    pl.List(file_path=list4, prec=1),
    pl.List(file_path=list5, prec=1),
    pl.List(file_path=list6, prec=1),
    pl.List(file_path=list7, prec=1),
    pl.List(file_path=list8, prec=1),
    pl.List(file_path=list9, prec=1),
    pl.List(file_path=list10, prec=1),
    pl.List(file_path=list11, prec=1),
]

# for row in tl.optimal_list(lists, original, backup):
#     print(row)
    
schedule = tl.optimal_list(lists, original, backup)
schedule_csv = '/Users/chibangnguyen/Documents/TiLearn/test/schedule.csv'

header = ['Name', 'p', 'r', 'd', 'w', 'p-factor']
with open(schedule_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(schedule)