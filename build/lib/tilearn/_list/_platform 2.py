import tilearn as tl
from tilearn import data
import numpy as np
import os

class List:
    def __init__(self, data, prec=1):
        self.data = data
        self.prec = prec
    
    def info(self):
        return self.data
    
    def check(self):
        return self.prec
    
    def run(self):
        if self.prec == 1:
            return tl.sum_factor(self.data)
        elif self.prec == 0:
            return tl.factor_data(self.data)
    
def ja_all(path, lists):
    sum = 0
    folder_path = path
    csv_count = len([file for file in os.listdir(folder_path) if file.endswith('.csv')])
    for i in range(csv_count):
        count = sum + tl.job_amount(lists[i].info())
        sum = count
    return count

def opt_loca(lists, pick):
    """
    Returns
    -------
    List
        opt = [sublist, row]
    """
    opt = tl.list_gen(2, 1)
    max_value = 0
    init = 0
    for sublist in lists:
        for i in range(tl.job_amount(sublist.info())):
            if sublist.run()[i][5] > max_value:
                max_value = sublist.run()[i][5]
                opt[0] = init
                opt[1] = i
        init += 1
    if pick == 'sub':
        return opt[0]
    elif pick == 'row':
        return opt[1]+1

def set_const(lists, prec):
    if prec == 1:
        set = tl.list_gen(opt_loca(lists, pick='row'), 6)
        opt_list = lists[opt_loca(lists, pick='sub')].run()
        for i in range(len(set)):
            for j in range(len(set[i])):
                set[i][j] = opt_list[i][j]
    # elif prec == 0:
    #     set = ['Job', 0, 0, 0, 0, 0]
    #     opt_list = lists[opt_loca(lists, pick='sub')].run()
    #     specific_row = opt_list[opt_loca(lists, pick='row')-1]
    #     set = specific_row[:len(set)] 
    return set

def optimal_list(path, lists):
    set_j = []
    jc = ja_all(path, lists)
    while jc > 0:
        opt_list = lists[opt_loca(lists, pick='sub')].run()
        if lists[opt_loca(lists, pick='sub')].check() == 1:
            row_list = opt_loca(lists, pick='row')
            set_j.extend(set_const(lists, 1))
            del opt_list[0:row_list]
            jc -= row_list
        # elif lists[opt_loca(lists, pick='sub')].check() == 0:
        #     row_list = opt_loca(lists, pick='row')
        #     set_j.extend(set_const(lists, 0))
        #     # del opt_list[row_list]
        #     opt_list = np.delete(opt_list, row_list, axis=0)
        #     jc -= 1
    return set_j