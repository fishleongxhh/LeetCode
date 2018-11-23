# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode191: Number of 1 Bits问题

import sys

#普通法
def hammingWeight(n):
    cnt = 0
    for i in range(32):
        cnt += (n&1)
        n >>= 1
    return cnt

#快速法
def hammingWeight2(n):
    cnt = 0
    while n:
        n &= (n-1) #n与n-1按位取与会消去n二进制表示中最右侧的1
        cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(n)
    print(bin(n))
    print(sum([int(i) for i in bin(n)[2:]]), hammingWeight2(n))
