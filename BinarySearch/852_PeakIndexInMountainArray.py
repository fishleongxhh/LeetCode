# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode852: Peak Index in a Mountain Array问题，需要用到二分查找

#这里的A保证是一个Mountain数组，现要求出其山峰的位置
def peakIndexInMountainArray(A):
    n = len(A)
    if n < 3:
        return -1
    low, high = 0, n-1
    while low <= high:
        middle = int((low+high)/2)
        index1 = (A[middle] > A[middle-1])
        index2 = (A[middle] > A[middle+1])
        if index1 and index2:
            return middle
        if index1 and (not index2):
            low = middle #这里不能+1！！否则可能数组越界
        if (not index1) and index2:
            high = middle #这里不能-1！！否则可能数组越界
    return -1

def peakIndexInMountainArray2(A):
    n = len(A)
    if n < 3:
        return -1
    low, high = 0, n-1
    while low < high:
        middle = int((low+high)/2)
        if A[middle] < A[middle+1]:
            low = middle + 1
        else:
            high = middle
    return low

if __name__ == "__main__":
    A = [1,5,4,3,2,1]
    print(A)
    print(peakIndexInMountainArray(A))
    print(peakIndexInMountainArray2(A))
