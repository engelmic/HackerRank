#!/bin/python3

import sys

def con_bin(i):
    x = bin(i)[2:]
    max = 0
    counter = 0
    last = True
    for c in str(x):
        if (int(c)) == 1:
            counter += 1
            last = True
            if max < counter:
                max = counter
            
        if int(c) == 0:
            counter = 0
            last = False    

    print(max)

con_bin(13)
con_bin(951)
con_bin(439)

