# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode268: Missing Number问题

#解法1
#任何整数与0按位异或都是它自己，与它自己按位异或都是0
def missingNumber(nums):
    res = 0
    for item in nums:
        res ^= item
    for item in range(len(nums)+1):
        res ^= item
    return res

#解法2
#简单运用加减法
def missingNumber2(nums):
    n = len(nums)
    mySum = n*(n+1)//2
    return mySum - sum(nums)

if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(nums)
    print(missingNumber(nums), missingNumber2(nums))
