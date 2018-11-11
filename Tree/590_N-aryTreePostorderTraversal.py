# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode590: N-ary Tree Postorder Traversal问题

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorderCore(self, root, res):
        if root:
            for child in root.children:
                self.postorderCore(child, res)
            res.append(root.val)

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.postorderCore(root, res)
        return res
