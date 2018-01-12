#!/bin/python3

import sys

def multiplier(number):
    if isinstance(number, int) and (2 <= number <= 20):
        pass
    else:
        exit(0)
    inc = 1
    while inc < 11:
        print(number, "x", inc, "=", number*inc)
        inc += 1

n = int(input().strip())
multiplier(n)
