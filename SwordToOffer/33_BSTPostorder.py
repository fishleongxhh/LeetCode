# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解剑指offer33: 二叉搜索树的后序遍历序列

#序列中的元素都是不重复的
def CheckPostorderSequence(nums):
    if not nums:
        return True
    root, start = nums[-1], 0
    while nums[start] < root:
        start += 1
    left_flag = CheckPostorderSequence(nums[:start])
    for item in nums[start:-1]:
        if item < root:
            return False
    right_flag = CheckPostorderSequence(nums[start:-1])
    return left_flag and right_flag

if __name__ == "__main__":
    nums = [5,7,6,8,3,4]
    print(nums)
    print(CheckPostorderSequence(nums))
