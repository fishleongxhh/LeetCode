# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode448. Find All Numbers Disappeared in an Array问题

from numpy.random import choice

#解法一：
def findDisappearedNumbers1(nums):
    n = len(nums)
    for loc in range(n):
        item = nums[loc]
        while loc != (item-1):
            if nums[item-1] == item:
                break
            else:
                nums[item-1], nums[loc] = nums[loc], nums[item-1]
                item = nums[loc]
    res = [loc+1 for loc in range(n) if nums[loc]!=(loc+1)]
    return res

#解法2
def findDisappearedNumbers2(nums):
    return list(set(range(1,len(nums)+1)) - set(nums))

if __name__ == "__main__":
    nums = [1,3,4,4]
    print(sorted(nums))
    print(findDisappearedNumbers1(nums[:]))
    print(findDisappearedNumbers2(nums[:]))
