# -*- coding: utf-8 -*-

import sys

while True:
    line = sys.stdin.readline().strip()
    if line == "END":
        break
    print(eval(line))
