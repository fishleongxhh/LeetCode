# -*- coding: utf-8 -*-
# Author: Xu Hanhui
#此程序用来求解LeetCode441: Arranging Coins问题

import sys

def arrangeCoins(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    low, high = 1, n
    while low <= high:
        middle = int((low+high)/2)
        item1, item2 = (middle+1)*middle/2, (middle+1)*(middle+2)/2
        if item1 > n:
            high = middle - 1
        else:
            if item2 > n:
                return middle
            else:
                low = middle + 1
    return -1

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(n, arrangeCoins(n))
