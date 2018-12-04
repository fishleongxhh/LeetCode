# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode643. Maximum Average Subarray I问题

#1 <= k <= len(nums) <= 30,000.
def findMaxAverage(nums, k):
    if not nums:
        return 0
    CurrSum = MaxSum = sum(nums[:k])
    for i in range(k, len(nums)):
        CurrSum = CurrSum - nums[i-k] + nums[i]
        if CurrSum > MaxSum:
            MaxSum = CurrSum
    return MaxSum/k

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 1
    print(nums)
    print(k)
    print(findMaxAverage(nums, k))
