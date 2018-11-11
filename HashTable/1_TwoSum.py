# -*- coding: utf-8 -*-
# Author: Xu Hanhui
#此程序用来求解LeetCode1: Two Sum问题，需要用到哈希映射

def twoSum(nums, target):
    my_dict = {}
    for i, element in enumerate(nums):
        if (target - element) in my_dict:
            return [my_dict[target-element], i]
        my_dict[element] = i
    return [-1, -1]

if __name__ == "__main__":
    nums = [7, 11, 2, 15]
    target = 13
    print(nums)
    print(target)
    print(twoSum(nums, target))
