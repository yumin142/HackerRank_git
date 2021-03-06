#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    # Write your code here
    dic = {}
    
    for i in set(parent[1:]):
        for j in range(i+1, len(parent)):
            if parent[j] == i:
                if i not in dic:
                    dic[i] = [j]
                else:
                    dic[i].append(j)
                    
    def recur(node):
        total = 0
        if node not in dic:
            return files_size[node]
        else:
            for i in dic[node]:
                total += recur(i)
            return total + files_size[node]
    
    sumfs = sum(files_size)
    diff = sumfs
    
    for node in range(1, len(parent)):
        # diff = min(diff, abs(recur(node) - (sum(files_size) - recur(node))))
        diff = min(diff, abs(2*recur(node) - sumfs))
    return diff
        
        
if __name__ == '__main__':
    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    print(result)
    
# TEST CASES:
# INPUT(0):
10
-1
0
1
2
1
0
5
2
0
0
10
8475
6038
8072
7298
5363
9732
3786
5521
8295
6186

# EXPECTED OUTPUT(0):
# 4182


# INPUT(1):
10
-1
0
0
0
0
3
4
6
0
3
10
298
2187
5054
266
1989
6499
5450
2205
5893
8095

# EXPECTED OUTPUT(1):
# 8216


zx:
def mostBalancedPartition(parent, files_size):

    parent_len = len(parent)
    children = [[] for i in range(parent_len)]
    for i in range(1, parent_len):
        children[parent[i]].append(i)

    size_sums = [0 for i in range(parent_len)]
    def size_sum(i):
        size_sums[i] = files_size[i] + sum(size_sum(k) for k in children[i])
        return size_sums[i]

    size_sum(0)
    return min(abs(size_sums[0] - 2*n) for n in size_sums[1:])