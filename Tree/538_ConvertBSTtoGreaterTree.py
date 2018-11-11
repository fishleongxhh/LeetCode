# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode538: Convert BST to Greater Tree问题

from Tree import TreeNode, initTree, treeScan

def makeLarger(root, plus_val):
    if not root:
        return plus_val
    root.val += makeLarger(root.right, plus_val)
    plus_val = makeLarger(root.left, root.val)
    return plus_val

def convertBST(root):
    tree_sum = makeLarger(root, 0)
    return root

if __name__ == "__main__":
    nums = []
    root = initTree(nums)
    treeScan(root)
    root = convertBST(root)
    treeScan(root)
