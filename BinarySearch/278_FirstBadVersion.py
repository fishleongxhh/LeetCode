# -*- coding: utf-8 -*-
# Author: Xu Hanhui
#此程序用来求解LeetCode278: First Bad Version, 需要使用二分查找

def firstBadVersion(n):
    low, high = 1, n
    while low <= high:
        middle = int((low+high)/2)
        if isBadVersion(middle):
            if middle == 1 or (not isBadVersion(middle-1)):
                return middle
            else:
                high = middle - 1
        else:
            low = middle + 1
    return -1

def isBadVersion(i):
    return status[i-1]

status = [True, True, True]
if __name__ == "__main__":
    print(firstBadVersion(3))
