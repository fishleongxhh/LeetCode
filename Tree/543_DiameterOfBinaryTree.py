# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode543: Diameter of Binary Tree问题

from Tree import *

def diameterOfBinaryTreeCore(root):
    if root:
        leftRes = diameterOfBinaryTreeCore(root.left)
        rightRes = diameterOfBinaryTreeCore(root.right)
        maxDiameter = max(leftRes[0], rightRes[0], leftRes[1]+2+rightRes[1])
        maxPath = max(leftRes[1], rightRes[1]) + 1
        return (maxDiameter, maxPath)
    return (-1,-1)

def diameterOfBinaryTree(root):
    res = diameterOfBinaryTreeCore(root)
    if res[0] == -1:
        return 0
    return res[0]

if __name__ == "__main__":
    nums = []
    root = initTree(nums)
    print(preOrderScan(root))
    print(diameterOfBinaryTree(root))
