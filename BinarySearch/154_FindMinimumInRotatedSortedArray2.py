# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode152: Find Minimum in Rotated Sorted Array2问题

#此题假设旋转数组中可能有重复数字
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
        #当前中后的元素都相同时使用顺序查找
        if nums[start] == nums[mid] and nums[mid] == nums[end]:
            return min(nums[start:end+1])
        if nums[mid] <= nums[end]: #这里和下面的条件判断必须考虑到等于号！！
            end = mid
        elif nums[mid] >= nums[start]:
            start = mid

if __name__ == "__main__":
    nums = [1,3,3,5,1,1]
    print(nums)
    print(findMin(nums))
