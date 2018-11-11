# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode559: Maximum Depth of N-ary Tree问题

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        res = max([0] + [self.maxDepth(child) for child in root.children]) + 1
        return res

