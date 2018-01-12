#!/usr/bin/env python3
#
# def wordy(num):
#     lrtn = []
#     if 2 <= num <= 10:
#         while num > 0:
#             word = input().strip()
#             if len(word) < 10000:
#                 #for ltr in word:
#                 for ind, ltr in enumerate(word):
#                     pos = ind
#                     if not pos % 2:
#                         #print(ltr, end='')
#                         lrtn.append(ltr)
#
#                 #print("  ", end='')
#                 lrtn.append(" ")
#                 for ind, ltr in enumerate(word):
#                     pos = ind
#                     if pos % 2:
#                         #print(ltr, end='')
#                         lrtn.append(ltr)
#                 lrtn.append("\n")
#                 num -=1
#         for w in lrtn:
#             print(w, end='')
#
# #wordy("word")
#
#
# cases = int(input().strip())
# wordy(cases)

for num in range(int(input())):
    s = input()
    print(s[::2], s[1::2])
