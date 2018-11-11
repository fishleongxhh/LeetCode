# -*- coding: utf-8 -*-

import sys
import math

x, y = [int(i) for i in sys.stdin.readline().strip().split()]
N = int(math.sqrt(2*(x+y)+1/4)-1/2)
print(x,y,N)

flag, res, cnt = N, x, 0
while res != 0:
    if res <= flag:
        res = 0
    else:
        res -= flag
        flag -= 1
    cnt += 1
print(cnt)
