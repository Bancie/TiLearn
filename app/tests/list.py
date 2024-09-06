import tilearn as tl
from tilearn import data

lists = [
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data.csv'), prec=1),
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data2.csv'), prec=0),
    tl.List(data=data.read_file('/Users/chibangnguyen/Documents/TiLearn/app/tests/data3.csv'), prec=1)
]


# for sublist in lists:
#     for row in sublist.run():
#         print(row)

# print('\n')

# for row in tl.set_construct(lists):
#     print(row)

# print(tl.main_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))

for row in tl.optimal_list('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists):
    print(row)