# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode700: Search in a Binary Search Tree问题

from Tree import *

def searchBST(root, val):
    if root:
        if root.val == val:
            return root
        elif root.val > val:
            return searchBST(root.left, val)
        else:
            return searchBST(root.right, val)
    return None
