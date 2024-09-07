import tilearn as tl
from tilearn import _plat as pl
import os

# ╔═══════════════════════════════╗
# ║           set_const           ║
# ╚═══════════════════════════════╝
def set_prec(lists):
    set = tl.list_gen(pl.location(lists, type='row'), 6)
    opt_list = lists[pl.location(lists, type='sub')].run()
    for i in range(len(set)):
        for j in range(len(set[i])):
            if i == 0 and j == 0:
                set[i][j] = str(opt_list[i][j])
            set[i][j] = opt_list[i][j]
    return set
    
def set(lists):
    set = tl.list_gen(1, 6)
    opt_list = lists[pl.location(lists, type='sub')].run()
    opt_row = pl.location(lists, type='row')-1
    for i in range(len(set)):
        for j in range(len(set[i])):
            if i == 0 and j == 0:
                set[i][j] = str(opt_list[opt_row][j])
            set[i][j] = opt_list[opt_row][j]
    return set

def set_const(lists, prec):
    if prec == 1:
        return set_prec(lists)
    elif prec == 0:
        return set(lists)

# ╔═══════════════════════════════╗
# ║          optimal_list         ║
# ╚═══════════════════════════════╝
def prec_updated(lists, set_j, opt_list, row_list):
    set_j.extend(set_const(lists, prec=1))
    next = row_list + 1
    del opt_list[row_list:next]
    return opt_list
    # return set_j

def updated(lists, set_j, opt_list, row_list):
    set_j.extend(set_const(lists, prec=0))
    next = row_list + 1
    del opt_list[row_list:next]
    return opt_list
    # return set_j

def optimal_list(path, lists):
    set_j = []
    jc = int(pl.ja_all(path, lists))
    while jc > 0:
        opt_list = lists[pl.location(lists, type='sub')].run()
        row_list = pl.location(lists, type='row')
        check = lists[pl.location(lists, type='sub')].check()
        if check == 1:
            prec_updated(lists, set_j, opt_list, row_list)
            jc -= row_list
        elif check == 0:
            updated(lists, set_j, opt_list, row_list)
            jc -= 1
    return set_j