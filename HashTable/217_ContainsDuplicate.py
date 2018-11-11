# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode217: Contains Duplicate问题

def containsDuplicate(nums):
    my_set = set()
    for item in nums:
        if item in my_set:
            return True
        my_set.add(item)
    return False

if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(nums)
    print(containsDuplicate(nums))
