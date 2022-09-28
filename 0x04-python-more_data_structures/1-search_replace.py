#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for s in my_list:
        if s == search:
            new_list.append(replace)
        else:
            new_list.append(s)
    return (new_list)
