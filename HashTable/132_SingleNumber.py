# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode136: Single Number问题，需要用到HashTable

def singleNumber(nums):
    res = {}
    for item in nums:
        if item in res:
            del res[item]
        else:
            res[item] = 1
    return list(res.keys())[0]

if __name__ == "__main__":
    nums = [4,1,2,1,2,4,3]
    print(nums)
    print(singleNumber(nums))
