#!/usr/bin/python3
def no_c(my_string):
    i = 0
    if my_string[0] == 'C' or my_string[0] == 'c':
        my_string = my_string[1:]
    for chr in my_string:
        if chr == 'C' or chr == 'c':
           my_string = my_string[:i] + my_string[i+1:]
        i+=1
    return my_string
    
    
