# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此程序用来求解LeetCode53：连续子数组最大和问题，涉及到动态规划

def MaxSubArray(nums):
    ThisSum, MaxSum, MaxItem = 0, 0, nums[0]
    for item in nums:
        ThisSum += item
        if ThisSum > MaxSum:
            MaxSum = ThisSum
        if ThisSum < 0:
            ThisSum = 0
        if item > MaxItem:
            MaxItem = item
    if MaxItem < 0: #主要是为了探测出数组中所有元素都小于0这种情况
        return MaxItem
    else:
        return MaxSum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-1, -1]
    res = MaxSubArray(nums)
    print(res)
