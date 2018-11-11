# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode46: Permutations问题

#nums是包含不重复整数的列表
def permuteCore(nums, ind=0, res=[]):
    if ind >= len(nums):
        res.append(nums[:])
    for i in range(ind, len(nums)):
        nums[ind], nums[i] = nums[i], nums[ind]
        permuteCore(nums, ind+1, res)
        nums[ind], nums[i] = nums[i], nums[ind]

def permute(nums):
    res = []
    permuteCore(nums, 0, res)
    return res

if __name__ == "__main__":
    nums = []
    res = permute(nums)
    for item in res:
        print(item)
