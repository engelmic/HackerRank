#!/bin/python3

import sys

def diagonalDifference(a):
    mwidth = len(a)
    diag1 = 0
    diag2 = 0
    for coord in range(mwidth):
        diag1 += a[coord][coord]
        #print(diag1)
        
    for coord in range(mwidth):
        diag2 += a[coord][-(coord + 1)]
        #print(diag2)
        
    return(abs(diag1 - diag2))

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)

# sample input - calculate difference between diagonal sums
# first int is matrix width
# 3
# 11 2 4
# 4 5 6
# 10 8 -12