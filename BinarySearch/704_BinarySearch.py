# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode704: Binary Search问题

#数组nums中的数字升序排列，同时唯一，返回目标值的下标或者-1
def search(nums, target):
    start, end = 0, len(nums)-1
    mid = (start+end)//2
    while start <= end:
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start+end)//2
    return -1

if __name__ == "__main__":
    nums = []
    target = -1
    print(nums, target)
    print(search(nums, target))
