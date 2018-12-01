# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode581. Shortest Unsorted Continuous Subarray问题

#数组的长度至少为1
def findUnsortedSubarray(nums):
    n = len(nums)
    nums1 = nums[:]
    start, end = 1, 0
    #从前至后执行一次冒泡排序，将最大值上浮，同时记录最后受影响的元素位置
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            end = i+1
    #从后至前执行一次冒泡排序，将最小值下沉，同时记录最后受影响的元素位置
    for i in range(n-1,0,-1):
        if nums1[i] < nums1[i-1]:
            nums1[i], nums1[i-1] = nums1[i-1], nums1[i]
            start = i-1
    return end - start + 1

#下述算法是对上述解法的改进，主要是无需发生显式的元素交换，同时也可以省去原数组的拷贝
def findUnsortedSubarray2(nums):
    n = len(nums)
    start, end = n, 0
    Max, Min = nums[0], nums[-1]
    #从前至后执行一次冒泡排序，将最大值上浮，同时记录最后受影响的元素位置
    for i in range(1, n):
        if nums[i] < Max:
            end = i
        else:
            Max = nums[i]
    #从后至前执行一次冒泡排序，将最小值下沉，同时记录最后受影响的元素位置
    for i in range(n-2,-1,-1):
        if nums[i] > Min:
            start = i
        else:
            Min = nums[i]
    return max(0, end-start+1)

if __name__ == "__main__":
    nums = [0, 2, 3, 3, 4, 8, 9, 9, 15, 17]
    nums = [2]
    print(nums, len(nums))
    print(sorted(nums))
    print(findUnsortedSubarray2(nums))
    print(findUnsortedSubarray(nums))
