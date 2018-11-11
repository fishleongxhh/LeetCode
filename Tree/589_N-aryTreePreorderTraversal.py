# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode589: N-ary Tree Preorder Traversal问题

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorderCore(self, root, res):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            res.append(root.val)
            for child in root.children:
                self.preorderCore(child, res)

    def preorder(self, root):
        res = []
        self.preorderCore(root, res)
        return res
