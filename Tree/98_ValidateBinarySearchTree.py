# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode98: Validate Binary Search Tree问题

from Tree import *

def isValidBSTCore(root, low, high):
    if root:
        rootVal = root.val
        if rootVal <= low or rootVal >= high:
            return False
        tag = isValidBSTCore(root.left, low, rootVal) and isValidBSTCore(root.right, rootVal, high)
        return tag
    return True

def isValidBST(root):
    tag = isValidBSTCore(root, float('-inf'), float('inf'))
    return tag

if __name__ == "__main__":
    nums = [5,1,4,3,6]
    root = initTree(nums)
    print(preOrderScan(root))
    print(isValidBST(root))
