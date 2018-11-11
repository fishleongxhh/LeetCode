# -*- coding: utf-8 -*-
# 此程序用来求解剑指offer第3题: 数组中重复的数字

#长度为n的数组，其中的数字都在0-n-1之间
#找到任意一个重复的数字即可，如果没有，则返回-1
def duplicate(nums):
    if not nums:
        print("Array is Empty!")
        return -1
    n = len(nums)
    for item in nums:
        if item < 0 or item > n-1:
            print("Numbers Out of Range!")
            return -1
    for i in range(n):
        while i != nums[i]:
            m = nums[i]
            if nums[i] == nums[m]:
                return m
            nums[i], nums[m] = nums[m], m
    return -1

if __name__ == "__main__":
    nums = [2,3,1,0,2,5,3]
    print(sorted(nums))
    print(duplicate(nums))
