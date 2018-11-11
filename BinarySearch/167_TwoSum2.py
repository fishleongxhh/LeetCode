# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode167: Two Sum II - Input array is sorted问题，需要用到二分查找

#数组按照升序排列，找到两个元素之和为目标元素，数组中的同一个元素不能使用两次
def twoSum(numbers, target):
    min_index, max_index = 0, len(numbers)-1
    index1 = min_index
    while index1 < max_index and index1 >= min_index:
        low, high = index1+1, max_index
        while low <= high:
            middle = int((low+high)/2)
            this_sum = numbers[index1] + numbers[middle]
            if this_sum == target:
                return [index1+1, middle+1]
            elif this_sum > target:
                high = middle - 1
            else:
                low = middle + 1
        index1 += 1
    return [-1, -1]

#此题可以有更好的解法，用两个指针从两端往中间移动即可
def twoSum2(numbers, target):
    low, high = 0, len(numbers)-1
    while low < high:
        thisSum = numbers[low] + numbers[high]
        if thisSum == target:
            return [low+1, high+1]
        elif thisSum > target:
            high -= 1
        else:
            low += 1
    return [-1, -1]

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 18
    print(numbers, target)
    print(twoSum(numbers, target))
    print(twoSum2(numbers, target))
