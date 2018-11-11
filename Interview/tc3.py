# -*- coding: utf-8 -*-

import sys

X, Y, Z = [int(item) for item in sys.stdin.readline().strip().split()]

cnt = 0
for a in range(1, X+1):
    for b in range(1, Y+1):
        upper = min(a+b, Z+1)
        lower = max(b-a, a-b)
        cnt += (upper - lower - 1)

print(cnt)
