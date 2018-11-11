# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode404: SumOfLeftLeaves问题

from Tree import TreeNode
from Tree import initTree

def kenelLeftLeavesSum(root, left_flag):
    if root == None:
        return 0
    if (root.left == None) and (root.right == None):
        return root.val if left_flag else 0
    res_left = kenelLeftLeavesSum(root.left, True)
    res_right = kenelLeftLeavesSum(root.right, False)
    return res_left + res_right

def sumOfLeftLeaves(root):
    return kenelLeftLeavesSum(root, False)

if __name__ == "__main__":
    nums = [5,2]
    root = initTree(nums)
    print(sumOfLeftLeaves(root))
