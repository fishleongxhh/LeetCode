# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此程序用来求解LeetCode35: Search Insert Position问题，需要用到二分查找

#此函数主要是查找目标元素在一个升序数组中的位置，如果没有，返回应该插入的位置
#假设数组中没有重复元素
def searchInsert(nums, target):
    n = len(nums)
    if n == 0:
        return 0
    low, high = 0, n-1
    while low <= high:
        middle = int((low+high)/2)
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return low

if __name__ == '__main__':
    nums = [1,2,4,6,8,9,11,14,16,18,20,26,30]
    target = 21
    print(nums)
    print(target)
    print(searchInsert(nums, target))
