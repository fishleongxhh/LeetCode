# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode230: Kth Smallest Element in a BST问题

from Tree import *

def kthSmallestCore(root, k, res):
    if root:
        if len(res) < k:
            kthSmallestCore(root.left, k, res)
        if len(res) < k:
            res.append(root.val)
        if len(res) < k:
            kthSmallestCore(root.right, k, res)

def kthSmallest(root, k):
    if (not root) or k <= 0:
        return None
    res = []
    kthSmallestCore(root, k, res)
    if len(res) == k:
        return res[-1]
    return None

if __name__ == "__main__":
    nums = [5,1,4,2,6,8,9,7,0,3]
    rootNode = initTree(nums)
    print(sorted(nums))
    for k in range(len(nums)+2):
        print(k, kthSmallest(rootNode, k))
