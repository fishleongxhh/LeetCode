# -*- coding: utf-8 -*-

import sys

a, b, c = [int(i) for i in sys.stdin.readline().split(" ")]

res = max([a+b+c, a*b*c, a+b*c, b+a*c, c+a*b, (a+b)*c, (b+a)*c, (c+a)*b])

print(res)
