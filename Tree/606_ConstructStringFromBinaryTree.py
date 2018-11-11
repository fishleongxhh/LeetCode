# -*- coding: utf -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode606: Construct String from Binary Tree问题

from Tree import *

def tree2strCore(root, res):
    if root:
        res.append(str(root.val))
        if root.left or root.right:
            res.append('(')
            tree2strCore(root.left, res)
            res.append(')')
            if root.right:
                res.append('(')
                tree2strCore(root.right, res)
                res.append(')')

def tree2str(t):
    res = []
    tree2strCore(t, res)
    return ''.join(res)

if __name__ == "__main__":
    nums = [5,3,2,6]
    root = initTree(nums)
    print(tree2str(root))
