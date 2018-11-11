# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode136: Single Number问题

def singleNumber(nums):
    if nums:
        res = 0
        for item in nums:
            res ^= item
        return res
    return None

if __name__ == "__main__":
    nums = [1,3,1]
    print(sorted(nums))
    print(singleNumber(nums))
