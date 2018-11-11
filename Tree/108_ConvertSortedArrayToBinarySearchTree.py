# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode108: Convert Sorted Array to Binary Search Tree问题

from Tree import TreeNode
from Tree import initTree
from Tree import treeScan

def height(root):
    if not root:
        return 0, True
    else:
        left_h, left_flag = height(root.left)
        right_h, right_flag = height(root.right)
        h = max(left_h, right_h) + 1
        flag = left_flag & right_flag & (left_h - right_h >= -1) & (left_h - right_h <= 1)
        return [h, flag]

def isBalanced(root):
    return height(root)[1]

#输入的数组是严格单调递增的
def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[0:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

if __name__ == "__main__":
    nums = list(range(100))
    print(nums)
    root = sortedArrayToBST(nums)
    treeScan(root)
    print(isBalanced(root))
