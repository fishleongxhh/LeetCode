# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode26: Remove Duplicates from Sorted Array问题

def removeDuplicates(nums):
    n = len(nums)
    if n <= 1:
        return n
    start, end = 0, 1
    while end < n:
        if nums[end] != nums[start]:
            if end > start+1:
                nums[start+1], nums[end] = nums[end], nums[start+1]
            start += 1
        end += 1
    return start+1

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(nums)
    print(removeDuplicates(nums), nums)
