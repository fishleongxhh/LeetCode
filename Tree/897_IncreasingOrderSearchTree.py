# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode897: Increasing Order Search Tree问题

class TreeNode:
    def __init__ (self, x):
        self.val = x
        self.left = None
        self.right = None

#按照元素顺序，将其初始化为一个二叉查找树
def initTree(nodeArray):
    if not nodeArray:
        return None
    n = len(nodeArray)
    for loc, node in enumerate(nodeArray):
        if loc == n-1:
            node.left = node.right = None
        else:
            node.left = None
            node.right = nodeArray[loc+1]
    return nodeArray[0]

#中序遍历+先序遍历，或者中序遍历+后序遍历都可以唯一确定一棵二叉树，但是先序+后序不行
#先序遍历二叉树
def preOrderScan(rootNode, res=[]):
    if rootNode:
        preOrderScan(rootNode.left, res)
        res.append(rootNode)
        preOrderScan(rootNode.right, res)

def increasingBST(root):
    nums = []
    preOrderScan(root, nums)
    root = initTree(nums)
    return root
