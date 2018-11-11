# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode107:  Binary Tree Level Order Traversal问题

from Tree import TreeNode
from Tree import initTree
from Tree import treeScan

def update_dic(root, res, depth):
    if root:
        if depth == len(res):
            res.append([root.val])
        else:
            res[depth].append(root.val)
        update_dic(root.left, res, depth+1)
        update_dic(root.right, res, depth+1)

def levelOrderBottom(root):
    res = []
    update_dic(root, res, 0)
    res.reverse()
    return res

if __name__ == "__main__":
    nums = []
    root = initTree(nums)
    print(nums)
    print(levelOrderBottom(root))
