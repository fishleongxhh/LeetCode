# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode283: Move Zeroes问题

def moveZeroes(nums):
    start, end, n = -1, 0, len(nums)
    while end < n:
        if nums[end] != 0:
            if end != (start+1):
                nums[start+1], nums[end] = nums[end], nums[start+1]
            start += 1
        end += 1

if __name__ == "__main__":
    nums = [0,0,0,1,3,0,0,0,2,3,4,5,65,0,0,1,2,0]
    print(nums)
    moveZeroes(nums)
    print(nums)
