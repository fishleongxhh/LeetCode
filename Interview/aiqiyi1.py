# -*- coding: utf-8 -*-

import sys

N, M, P = [int(i) for i in sys.stdin.readline().strip().split()]
nums = [int(i) for i in sys.stdin.readline().strip().split()]

for day in range(M):
    flag, food = sys.stdin.readline().strip().split()
    if flag == 'A':
        nums[int(food)-1] += 1
    else:
        nums[int(food)-1] -= 1

rank, cnt = 1, nums[P-1]
for i in nums:
    rank = rank+1 if i > cnt else rank
print(nums,rank)
