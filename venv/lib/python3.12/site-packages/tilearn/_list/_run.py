import tilearn as tl
from tilearn import _plat as pl
from tilearn import _data as data
import os

def set_prec(lists, op, row):
    set = tl.list_gen(row, 6)
    for i in range(len(set)):
        for j in range(len(set[i])):
            if i == 0 and j == 0:
                set[i][j] = str(op[i][j])
            set[i][j] = op[i][j]
    return set
    
def set(lists, op, row):
    set = tl.list_gen(1, 6)
    fix_row = row
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

def file_seek(lists, path):
    sum = pl.count_file(path)
    for sublist in lists:
        if sublist.info() == []:
            sum -= 1
    return sum

def optimal_list(lists, path, backup_path):
    set_j = []
    data.backup(path, backup_path)
    jc = pl.ja_all(lists, path)
    while jc > 0:
        opt_list = lists[pl.location(lists, type='sub')].run()
        row_list = pl.location(lists, type='row')
        opt_file = lists[pl.location(lists, type='sub')].path
        check = lists[pl.location(lists, type='sub')].check()
        if check == 1:
            if file_seek(lists, path=backup_path) == 1:
                set_j.extend(opt_list)
                break
            set_j.extend(set_const(lists, prec=1, op=opt_list, row=row_list+1))
            data.updated(opt_file, prec=1, opt_row=row_list)
            jc -= row_list+1
        elif check == 0:
            set_j.extend(set_const(lists, prec=0, op=opt_list, row=row_list))
            data.updated(opt_file, prec=0, opt_row=row_list)
            jc -= 1
    data.clear(backup_path)
    return set_j