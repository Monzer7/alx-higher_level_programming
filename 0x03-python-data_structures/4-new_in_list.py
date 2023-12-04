#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        cp = my_list.copy()
        for i in range(len(my_list)):
            if i == idx:
                cp[i] = element
                return cp
