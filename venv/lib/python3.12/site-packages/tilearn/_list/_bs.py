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
            return tl.sum_factor(self.data)
        elif self.prec == 0:
            return tl.factor_data(self.data)
    
def job_amount_all(path, lists):
    sum = 0
    folder_path = path
    csv_count = len([file for file in os.listdir(folder_path) if file.endswith('.csv')])
    for i in range(csv_count):
        count = sum + tl.job_amount(lists[i].info())
        sum = count
    return count

def opt_loca(lists):
    """
    Returns
    -------
    List
        opt = [sublist location, list row location]
    """
    opt = tl.list_gen(2, 1)
    max_value = 0
    sl = -1
    for sublist in lists:
        sl += 1
        opt[0][0] = sl
        for i in range(tl.job_amount(sublist.info())):
            if sublist.run()[i][5] > max_value:
                max_value = sublist.run()[i][5]
                opt[1][0] = i
    return opt

# def main_list(path, lists):
#     set_j = []
#     while job_amount_all(path) == 0:
#         a