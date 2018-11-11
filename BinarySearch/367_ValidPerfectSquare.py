# -*- coding: utf-8 -*-
# Author: Xu Hanhui
#此程序用来求解LeetCode367: Valid Perfect Square问题，需要用到二分查找

import math

#这里总假设num>=0, 且为整数
def isPerfectSquare(num):
    low, high = 0, num
    while low <= high:
        middle = int((low+high)/2)
        tmp = middle*middle
        if tmp == num:
            return True
        elif tmp < num:
            low = middle + 1
        else:
            high = middle - 1
    return False

if __name__ == "__main__":
    for i in range(20):
        print(i, isPerfectSquare(i), math.sqrt(i))
