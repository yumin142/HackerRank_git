#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def authEvents(events):
    # Write your code here
    p = 131
    m = 10**9 + 7
    result = []
    for e in events:
        if e[0] == "setPassword":
            pw = list(e[1])
            # print('pw = ', pw)
            l = len(pw)
            ha = 0
            alt_ha = 0
            for i in range(l):
                ha += ord(pw[i]) * (p**(l-i-1))
                alt_ha += ord(pw[i]) * (p**(l-i))
            # print('ha = ', ha)
            # print('alt_ha =', alt_ha % m)
        elif e[0] == "authorize":
            au = int(e[1])
            # print('au = ', au)
            my_calc = ha % m
            # print('my_calc = ', my_calc)
            # print(my_calc == au)
            test = abs(au - alt_ha % m)
            if my_calc == au:
                result.append(1)
            elif (test >=48 and test <=57) or (test >=65 and test <=90) or (test >=97 and test <=122):
                result.append(1)
            else:
                result.append(0)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


Your Output (stdout)
1
1
0
0
1
1
1
1
0
1
0
1
1
1
1
0
0
0
1
0
0
1
1
0
0
1
1
1
1
0
0
1
1
1
0
0
1
1
1
0
1
0
0
1
1
0
0
1
0
0
0
0
0
0
1
0
1
1
1
1
1
1
0
0
0
1
0
1
0
0
0
0
0
1
1
1
0
0
1
1
0
0
1
1
1
1
0
1
0
1
0
1
1
0
0
1
0
1
0
1
1
1
1
1
0
1
0
0
0
0
0
1
0
1
0
0
1
1
1
1
0
0
0
0
0
1
0
1
1
0
0
0
1
0
0
1
0
1
1
1
1
1
0
0
1
1
0
0
1
0
1
1
1
1
1
0
0
0
1
1
1
1
0
1
1
0
1
1
0
1
0
1
0
1
0
1
0
1
0
0
1
1
1
0
1
0
1
0
0
1
0
0
0
1
0
1
0
1
0
0
0
0
1
1
1
1
1
0
1
1
1
1
1
1
1
0
1
1
1
0
0
1
0
0
1
1
0
0
0
0
0
0
0
0
1
1
0
0
0
1
0
1
0
1
1
1
0
1
1
1
0
1
1
0
0
1
1
0
1
0
0
0
1
1
1
0
1
1
1
1
0
1
0
0
1
1
0
1
0
1
0
1
1
1
0
0
0
1
1
0
0
1
1
0
1
0
0
0
1
1
0
1
1
0
0
1
1
0
1
0
0
1
0
1
0
1
0
0
1
0
0
0
0
1
1
1
0
0
0
1
1
1
1
0
1
1
1
1
0
1
1
1
0
1
0
0
0
1
0
0
0
1
1
0
1
0
1
1
1
0
1
1
1
1
1
0
0
1
1
1
1
1
0
1
1
1
0
1
0
1
1
0
0
1
1
1
1
0
1
1
1
1
1
0
0
0
1
0
1
0
1
0
1
1
0
0
1
0
0
1
0
0
0
1
1
1
0
1
1
1
0
0
0
0
1
0
1
1
1
0
1
1
1
0
0
1
0
1
0
1
1
1
1
0
1
1
1
1
0
1
1
0
0
1
1
1
1
1
1
1
0
1
0
1
1
0
0
1
1
0
0
0
1
0
1
0
1
1
0
1
0
1
1
1
1
0
0
0
0
0
1
1
1
0
0
0
0
1
1
1
1
0
1
1
1
0
0
0
1
0
0
1
0{-truncated-}