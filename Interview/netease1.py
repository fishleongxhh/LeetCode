# -*- coding: utf-8 -*-
# Author: Xu Hanhui

import sys
from collections import Counter

n, m = [int(i) for i in sys.stdin.readline().strip().split(" ")]
cols = [int(i) for i in sys.stdin.readline().strip().split(" ")]

cnt = Counter(cols)
if len(cnt.keys()) < n:
    print(0)
else:
    print(min(cnt.values()))
