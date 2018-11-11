# -*- coding: utf-8 -*-

import sys

test_num = int(sys.stdin.readline().strip())

for i in range(test_num):
    N, M = [int(item) for item in sys.stdin.readline().strip().split(" ")]
    if N == 1:
        if M == 1:
            print(1)
        else:
            print(M-2)
    else:
        if M == 1:
            print(N-2)
        else:
            print((M-2)*(N-2))
