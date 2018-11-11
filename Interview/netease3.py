# -*- coding: utf-8 -*-

import sys

def searchInsert(nums, target):
    n = len(nums)
    if n == 0:
        return 0
    low, high = 0, n-1 
    while low <= high:
        middle = int((low+high)/2)
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            high = middle - 1 
        else:
            low = middle + 1 
    return low

n = int(sys.stdin.readline().strip())
num = [int(i) for i in sys.stdin.readline().strip().split(" ")]
m = int(sys.stdin.readline().strip())
query_num = [int(i) for i in sys.stdin.readline().strip().split(" ")]

for i in range(1,n):
    num[i] = num[i] + num[i-1]

for item in query_num:
    print(searchInsert(num, item)+1)
