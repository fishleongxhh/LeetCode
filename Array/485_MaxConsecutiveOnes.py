# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode485: Max Consecutive Ones问题

from itertools import groupby

#nums的元素非0即1，且不为空
def findMaxConsecutiveOnes(nums):
    CurrLen = MaxLen = 0
    for item in nums:
        if item == 0:
            CurrLen = 0
        else:
            CurrLen += 1
            if CurrLen > MaxLen:
                MaxLen = CurrLen
    return MaxLen

if __name__ == "__main__":
    nums = [0,0,0,1,1,1,0,0,1,1]
    print(nums)
    print(max([len(list(group)) for name,group in groupby(nums) if name==1]))
    print(findMaxConsecutiveOnes(nums))
