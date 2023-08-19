#!/usr/bin/python3
def uniq_sum(my_list=None):
    if my_list is None:
        my_list = []
    return sum(set(my_list))
