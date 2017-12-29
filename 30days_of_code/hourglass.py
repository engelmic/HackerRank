#!/bin/python3

import sys


def hourglass(ar):
    iwidth = len(ar) - 2
    result = 0
    max_result = -64
    c_col = 0 # current leftmost column
    c_row = 0 # current upper row
    for num2 in range(iwidth):
        c_row = num2
        for num in range(iwidth):
            c_col = num
            for i in ar[c_row][c_col:c_col+3]:
                result += i

            #print(c_col)

            result += ar[c_row + 1][c_col + 1]

            for i in ar[c_row + 2][c_col:c_col+3]:
                result += i

            if result > max_result:
                max_result = result
            
            #print(result)
            result = 0

# all of these lines test the very first hourglass, not sure how to increment them yet
    # for i in ar[0][0:3]:
    #     result += i
 
    # result += ar[1][1]
 
    # for i in ar[2][0:3]:
    #     result += i
# all of these lines test the very first hourglass, not sure how to increment them yet

    print(max_result)


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

hourglass(arr)

# sample input (6x6 grid) converted to 2d array (arr) by for loop below array declaration
# I added functionality to accept any grid size with iwidth
# -1 -1 0 -9 -2 -2
# -2 -1 -6 -8 -2 -5
# -1 -1 -1 -2 -3 -4
# -1 -9 -2 -4 -4 -5
# -7 -3 -3 -2 -9 -9
# -1 -3 -1 -2 -4 -5