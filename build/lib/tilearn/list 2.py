import tilearn as tl
from tilearn import data
import os

class List:
    def __init__(self, data, prec=1):
        self.data = data
        self.prec = prec
    
    def info(self):
        return self.data
    
    def run(self):
        if self.prec == 1:
            return tl.wspt_prec(self.data)
        elif self.prec == 0:
            return tl.wspt(self.data)
    
        
lists = [
    List(data=data.read_file('app/tests/data.csv'), prec=1),
    List(data=data.read_file('app/tests/data2.csv'), prec=1)
]


def job_amount_all(path, lists):
    sum = 0
    folder_path = path
    csv_count = len([file for file in os.listdir(folder_path) if file.endswith('.csv')])
    for i in range(csv_count):
        count = sum + tl.job_amount(lists[i].info())
        sum = count
    return count

def mixed(path, lists):
    set_j = tl.list_gen(0, 6)
    max = 0
    position = 0
    sl = -1
    for sublist in lists:
        sub_pst = sl + 1
        for i in range(tl.job_amount(sublist.info())):
            if sublist.run()[i][5] > max:
                max = sublist.run()[i][5]
                position = i
        
# for sublist in lists:
#     print(sublist.run())
# print(mixed('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists))
# print(lists[1].run())
# print(tl.list_gen(job_amount_all('/Users/chibangnguyen/Documents/TiLearn/app/tests', lists), 6))