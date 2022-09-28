#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_mul = a_dictionary.copy()
    for key in new_mul.keys():
        new_mul[key] = new_mul[key] * 2
    return new_mul
