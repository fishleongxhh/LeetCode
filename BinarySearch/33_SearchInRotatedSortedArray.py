# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode33. Search in Rotated Sorted Array问题

#找到nums中的转折点
#如果没有转折点，则返回-1
def findPivot(nums):
    n = len(nums)
    start, end = 0, n-1
    #如果nums长度为0或者长度为1或者是单调递增的，则返回-1
    if (not nums) or (nums[end] >= nums[start]):
        return -1
    mid = -1
    while start <= end:
        mid = (start+end)//2
        if mid > 0 and nums[mid] < nums[mid-1]:
            break
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid - 1
    return mid

#在升序数组中查找某个元素,若未找到则返回-1
#start和end必须要合理，即处于0和n-1之间
def findTarget(nums, start, end, target):
    if start < 0 or end > len(nums)-1 or start > end:
        return -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

#nums中的元素都是唯一的，不重复的
def search(nums, target):
    n = len(nums)
    pivotLoc = findPivot(nums)
    if pivotLoc == -1:
        res = findTarget(nums, 0, n-1, target)
    elif target > nums[-1]:
        res = findTarget(nums, 0, pivotLoc-1, target)
    else:
        res = findTarget(nums, pivotLoc, n-1, target)
    return res

def listFind(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,8,9,10]
    nums = []
    print(nums)
    print(findPivot(nums))
    for target in [-1, 0, 5, 6.5, 8.5, 9, 10, 13]:
        print(target, search(nums, target), listFind(nums, target))
