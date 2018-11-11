# -*- coding: utf-8 -*-
# Author: Xu Hanhui

import sys

n, k = [int(i) for i in sys.stdin.readline().strip().split(" ")]
score = [int(i) for i in sys.stdin.readline().strip().split(" ")]
flag = [int(i) for i in sys.stdin.readline().strip().split(" ")]
print(score)
print(flag)

zero_loc = [i for i in range(n) if flag[i]==0]
one_score_sum = sum([item for i,item in enumerate(score) if flag[i]==1])
max_score = 0

for i,loc in enumerate(zero_loc):
    curr_score, end = 0, min(loc+k, n)
    for start in zero_loc[i:]:
        if start < end:
            curr_score = curr_score + score[start]
        else:
            break
    max_score = max(max_score, curr_score)
    if end == n:
        break

print(max_score+one_score_sum)
