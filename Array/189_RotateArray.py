# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode189: Rotate Array问题

def rotate(nums, k):
    n = len(nums)
    k = k%n
    nums[:k], nums[k:] = nums[n-k:], nums[:n-k]

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 6
    print(nums, k)
    rotate(nums, k)
    print(nums)
