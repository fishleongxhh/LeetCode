# -*- coding: utf-8 -*-
#此程序用来求解美团点评2018秋招笔试全1串问题

import sys
import numpy as np
import time

N, K = 500000, 50
data = list(np.random.choice([0,1], N, replace=True))
#N, K = [int(i) for i in sys.stdin.readline().strip().split(' ')]
#data = [int(i) for i in sys.stdin.readline().strip().split(' ')]

print(N, K)
#print(data)

print(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())))

max_len = 0
for loc in range(0,max(N-K,1),1):
    start = end = loc
    zero_num = 0
    while end <= (len(data)-1) and zero_num < K:
        if data[end] == 0:
            zero_num += 1
        end += 1
    while end <= len(data)-1 and data[end] == 1:
        end += 1
    max_len = max(max_len, end-start)
print(max_len)

print(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())))

max_len = 0
start = end = 0
n, zero_num = len(data), 0
while start <= n - 1:
    while end <= n - 1 and zero_num < K:
        if data[end] == 0:
            zero_num += 1
        end += 1
    while end <= n - 1 and data[end] == 1:
        end += 1
    max_len = max(max_len, end-start)
    if end > n:
        break
    while start <= n - 1 and data[start] == 1:
        start += 1
    if start <= n - 1 and data[start] == 0:
        start += 1
        zero_num -= 1
print(max_len)

print(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())))
