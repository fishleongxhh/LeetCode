# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode100: Same Tree问题

from Tree import TreeNode
from Tree import initTree
from Tree import treeScan

def isSameTree(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    if p.val != q.val:
        return False
    if not isSameTree(p.left, q.left):
        return False
    if not isSameTree(p.right, q.right):
        return False
    return True

if __name__ == "__main__":
    nums1 = []
    print(nums1)
    rootNode1 = initTree(nums1)
    treeScan(rootNode1)
    nums2 = []
    print(nums2)
    rootNode2 = initTree(nums2)
    treeScan(rootNode2)
    print(isSameTree(rootNode1, rootNode2))


