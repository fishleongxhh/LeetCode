# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode27: Remove Element问题

def removeElement(nums, val):
    n = len(nums)
    if n < 1:
        return 0
    start, end = -1, 0
    while end < n:
        if nums[end] != val:
            if end != start+1:
                nums[start+1], nums[end] = nums[end], nums[start+1]
            start += 1
        end += 1
    return start+1

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 0
    print(nums, val)
    print(removeElement(nums,val), nums)
