#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, m = 0, 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                m = m + 1
        except (ValueError, NameError):
            continue
    print()
    return m
