# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode226: Invert Binary Tree问题

from Tree import TreeNode
from Tree import initTree
from Tree import treeScan

def invertTree(root):
    if (root == None) or (root.left==None and root.right==None):
        return root
    root.left = invertTree(root.left)
    root.right = invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root

if __name__ == "__main__":
    nums = []
    root = initTree(nums)
    treeScan(root)
    root = invertTree(root)
    treeScan(root)
