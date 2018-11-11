# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode671: Second Minimum Node In a Binary Tree问题

from Tree import *

def findSecondMinimumValueCore(root, mininum, res):
    if root:
        if root.val > mininum and root.val < res:
            res = root.val
        res = findSecondMinimumValueCore(root.left, mininum, res)
        res = findSecondMinimumValueCore(root.right, mininum, res)
    return res

def findSecondMinimumValue(root):
    if not root:
        return -1
    mininum, res = root.val, float('inf')
    res = findSecondMinimumValueCore(root, mininum, res)
    if res == float('inf'):
        return -1
    else:
        return res

if __name__ == "__main__":
    nums = [3,3,5]
    print(nums)
    root = initTree(nums)
    print(preOrderScan(root))
    print(findSecondMinimumValue(root))
