import tilearn as tl
from tilearn import _plat as pl
from tilearn import _data as data
import os

def set_prec(lists, op, row):
    set = tl.list_gen(row, 6)
    # opt_list = lists[pl.location(lists, type='sub')].run()
    for i in range(len(set)):
        for j in range(len(set[i])):
            if i == 0 and j == 0:
                set[i][j] = str(op[i][j])
            set[i][j] = op[i][j]
    return set
    
def set(lists, op, row):
    set = tl.list_gen(1, 6)
    # opt_list = lists[pl.location(lists, type='sub')].run()
    # opt_row = pl.location(lists, type='row')-1
    fix_row = row - 1
    for i in range(len(set)):
        for j in range(len(set[i])):
            if i == 0 and j == 0:
                set[i][j] = str(op[fix_row][j])
            set[i][j] = op[fix_row][j]
    return set

def set_const(lists, prec, op, row):
    if prec == 1:
        return set_prec(lists, op, row)
    elif prec == 0:
        return set(lists, op, row)

def optimal_list(lists, path, backup_path):
    set_j = []
    # data.backup(path, backup_path)
    jc = pl.ja_all(lists, path)
    while jc > 0:
        opt_list = lists[pl.location(lists, type='sub')].run()
        row_list = pl.location(lists, type='row')
        opt_file = lists[pl.location(lists, type='sub')].path
        check = lists[pl.location(lists, type='sub')].check()
        if check == 1:
            set_j.extend(set_const(lists, prec=1, op=opt_list, row=row_list))
            data.updated(opt_file, prec=1, opt_row=row_list)
            jc -= row_list
        elif check == 0:
            set_j.extend(set_const(lists, prec=0, op=opt_list, row=row_list))
            data.updated(opt_file, prec=0, opt_row=row_list)
            jc -= 1
        print(opt_list, '\n')
        # print(row_list, '\n')
        # print(opt_file, '\n')
        # print(check, '\n')
    data.clear(backup_path)
    # return set_j