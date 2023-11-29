#!/usr/bin/python3
def islower(c):
    s = ord(c)
    for i in range(97, 123):
        if i == s:
            return True
        else:
            return False
