# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode101: Symmetric Tree问题

from Tree import TreeNode
from Tree import initTree
from Tree import preOrderScan
from Tree import midOrderScan
from Tree import postOrderScan
from Tree import treeScan

def LeftRightSymmetric(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    return (p.val == q.val) and LeftRightSymmetric(p.left, q.right) and LeftRightSymmetric(p.right, q.left)

def isSymmetric(root):
    if root == None:
        return True
    return LeftRightSymmetric(root.left, root.right)

if __name__ == "__main__":
    nums = [5,1,3,6,8,9]
    root = initTree(nums)
    treeScan(root)
    print(isSymmetric(root))
