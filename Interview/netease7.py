# -*- coding: utf-8 -*-

import sys

n, m, k = [int(i) for i in sys.stdin.readline().strip().split(" ")]

data = ['a']*n + ['z']*m

if k > (1+m*n):
    print(-1)
else:
    start = n-1
    k = k - 1
    while k > 0:
        move = min(k, m)
        data[start], data[start+move] = data[start+move], data[start]
        k = k-move
        start -= 1
    print(''.join(data))
