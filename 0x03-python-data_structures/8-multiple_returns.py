#!/usr/bin/python3
def multiple_returns(sentence):
    c = len(sentence)
    s = None
    if c != 0:
        s = sentence[0]
    return c, s
