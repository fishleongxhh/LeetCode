# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode104: Maximum Depth of Binary Tree问题

from Tree import TreeNode
from Tree import initTree
from Tree import treeScan

def maxDepth(root):
    if root == None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

if __name__ == "__main__":
    nums = []
    print(nums)
    root = initTree(nums)
    treeScan(root)
    print(maxDepth(root))
