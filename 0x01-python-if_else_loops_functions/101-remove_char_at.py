#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        m = str[:n] + str[n+1:]
    elif n < 0:
        m = str
    return m
