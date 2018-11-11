# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode872: Leaf-Similar Trees问题

from Tree import *

def getLeafNodes(root, res):
    if root:
        if (not root.left) and (not root.right):
            res.append(root.val)
        else:
            getLeafNodes(root.left, res)
            getLeafNodes(root.right, res)

def leafSimilar(root1, root2):
    res1, res2 = [], []
    getLeafNodes(root1, res1)
    getLeafNodes(root2, res2)
    return res1 == res2

if __name__ == "__main__":
    nums1 = [5,3]
    nums2 = [6,3,7]
    root1 = initTree(nums1)
    root2 = initTree(nums2)
    print(leafSimilar(root1,root2))
