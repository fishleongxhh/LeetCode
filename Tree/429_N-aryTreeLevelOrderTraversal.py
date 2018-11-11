# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode429: N-ary Tree Level Order Traversal问题

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from Tree import TreeNode
from Tree import initTree

def levelOrderKernel(root, res, depth):
    if root:
        if len(res) == depth:
            res.append([root.val])
        else:
            res[depth].append(root.val)
        for child in root.children:
            levelOrderKernel(child, res, depth+1)

def levelOrderKernel2(root, res, depth):
    if not root:
        return res
    if len(res) == depth:
        res.append([root.val])
    else:
        res[depth].append(root.val)
    for child in root.children:
        res = levelOrderKernel2(child, res, depth+1)
    return res


def levelOrder(root):
    res = levelOrderKernel2(root, [], 0)
    return res


