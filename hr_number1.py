#!/bin/python3

import sys


N = int(input().strip())

if N % 2 != 0:
    print("Weird")
    exit(0)
if 2 <= N <= 5 or N > 20:
    print("Not Weird")
if 6 <= N <= 20:
    print("Weird")