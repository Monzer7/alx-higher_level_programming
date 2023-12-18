#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    m = 0
    try:
        while m < x:
            print("{}".format(my_list[m]), end="")
            m = m + 1
        print()
    except IndexError:
        print()
        return m
    return m
