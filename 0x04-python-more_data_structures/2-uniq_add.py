#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    for uniq in set(my_list):
        uniq_sum += uniq
    return (uniq_sum)
