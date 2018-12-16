# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode34. Find First and Last Position of Element in Sorted Array问题

#在升序数组中查找某个元素,若未找到则返回-1
#start和end必须要合理，即处于0和n-1之间
def findStart(nums, start, end, target):
    if start < 0 or end > len(nums)-1 or start > end:
        return -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            if mid == start or nums[mid-1] < nums[mid]:
                return mid
            else:
                end = mid #这个地方要格外注意！！
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def findEnd(nums, start, end, target):
    if start < 0 or end > len(nums)-1 or start > end:
        return -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            if mid == end or nums[mid+1] > nums[mid]:
                return mid
            else:
                start = mid+1 #这个地方要格外注意！！
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def searchRange(nums, target):
    n = len(nums)
    start = findStart(nums, 0, n-1, target)
    if start == -1:
        return [-1,-1]
    end = findEnd(nums, 0, n-1, target)
    return [start, end]

if __name__ == "__main__":
    nums = [2,2]
    print(nums)
    for target in nums + [0,1,2,3,4,6,9,11]:
        print(target, searchRange(nums, target))
