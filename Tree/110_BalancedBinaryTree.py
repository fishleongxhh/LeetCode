# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode110: Balanced Binary Tree问题

from Tree import TreeNode
from Tree import initTree

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

if __name__ == "__main__":
    nums = [5, 2, 1, 7, 6, 8, 9, 0]
    root = initTree(nums)
    print(nums)
    print(isBalanced(root))
