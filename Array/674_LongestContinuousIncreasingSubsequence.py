# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode674. Longest Continuous Increasing Subsequence问题

def findLengthOfLCIS(nums):
    if not nums:
        return 0
    CurrLen = MaxLen = 1
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            CurrLen += 1
        else:
            CurrLen = 1
        if CurrLen > MaxLen:
            MaxLen = CurrLen
    return MaxLen

if __name__ == "__main__":
    nums = [5,2,54,224,5,2,4,14,42,54,21,1,3,1,41,4,3,552,4,12,4]
    print(nums)
    print(findLengthOfLCIS(nums))
