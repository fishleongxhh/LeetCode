# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode153: Find Minimum in Rotated Sorted Array问题

#此题假设旋转数组中没有重复数字
def findMin(nums):
    start, end = 0, len(nums)-1
    if end < start:
        return None
    if nums[end] > nums[start] or start == end:
        return nums[start]
    while start < end:
        if end - start == 1:
            return nums[end]
        mid = (start+end)//2
        if nums[mid] < nums[end]: #由于元素没有重复，这里和下面的条件判断可以考虑等于号也可以不考虑
            end = mid
        elif nums[mid] > nums[start]:
            start = mid

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    print(nums)
    print(findMin(nums))
