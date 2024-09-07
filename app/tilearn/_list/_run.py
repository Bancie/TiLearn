import tilearn as tl
from tilearn import _plat as pl
import numpy as np
import os

# ╔═══════════════════════════════╗
# ║           set_const           ║
# ╚═══════════════════════════════╝
def set_prec(lists):
    set = tl.list_gen(pl.opt_loca(lists, pick='row'), 6)
    opt_list = lists[pl.opt_loca(lists, pick='sub')].run()
    for i in range(len(set)):
        for j in range(len(set[i])):
            set[i][j] = opt_list[i][j]
    return set
    
def set_non(lists):
    set = ['Job', 0, 0, 0, 0, 0]
    opt_list = lists[pl.opt_loca(lists, pick='sub')].run()
    specific_row = opt_list[pl.opt_loca(lists, pick='row')-1]
    set = specific_row[:len(set)] 
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
    set_j.extend(set_const(lists, 1))
    del opt_list[0:row_list]
    return opt_list

# def non_updated():

def optimal_list(path, lists):
    set_j = []
    jc = pl.ja_all(path, lists)
    while jc > 0:
        opt_list = lists[pl.opt_loca(lists, pick='sub')].run()
        check = lists[pl.opt_loca(lists, pick='sub')].check()
        if check == 1:
            row_list = pl.opt_loca(lists, pick='row')
            prec_updated(lists, set_j, opt_list, row_list)
            jc -= row_list
        # elif lists[pl.opt_loca(lists, pick='sub')].check() == 0:
        #     row_list = pl.opt_loca(lists, pick='row')
        #     set_j.extend(set_const(lists, 0))
        #     # del opt_list[row_list]
        #     opt_list = np.delete(opt_list, row_list, axis=0)
        #     jc -= 1
    return set_j