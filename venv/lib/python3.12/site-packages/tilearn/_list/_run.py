import tilearn as tl
from tilearn import _plat as pl
import numpy as np
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
    
def set_non(lists):
    set = ['', 0, 0, 0, 0, 0]
    opt_list = lists[pl.location(lists, type='sub')].run()
    opt_row = opt_list[pl.location(lists, type='row')-1]
    for i in range(len(set)):
        if i == 0:
            set[i] = str(opt_row[i])
        set[i] = opt_row[i]
    return set

def set_const(lists, prec):
    if prec == 1:
        return set_prec(lists)
    elif prec == 0:
        return set_non(lists)

# ╔═══════════════════════════════╗
# ║          optimal_list         ║
# ╚═══════════════════════════════╝
def prec_updated(lists, set_j, opt_list, row_list):
    set_j.extend(set_const(lists, prec=1))
    del opt_list[0:row_list]
    return opt_list

# def non_updated():

def optimal_list(path, lists):
    set_j = []
    jc = pl.ja_all(path, lists)
    while jc > 0:
        opt_list = lists[pl.location(lists, type='sub')].run()
        check = lists[pl.location(lists, type='sub')].check()
        # if check == 1:
        row_list = pl.location(lists, type='row')
        prec_updated(lists, set_j, opt_list, row_list)
        jc -= row_list
        # elif lists[pl.location(lists, type='sub')].check() == 0:
        #     row_list = pl.location(lists, type='row')
        #     set_j.extend(set_const(lists, 0))
        #     # del opt_list[row_list]
        #     opt_list = np.delete(opt_list, row_list, axis=0)
        #     jc -= 1
    return set_j