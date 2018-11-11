# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode257: Binary Tree Paths问题

from Tree import TreeNode
from Tree import initTree

def allPaths(root, res=['']):
    if root == None:
        return []
    if root.left == None and root.right == None:
        res[0] = res[0] + str(root.val)
        return res
    res[0] = res[0] + str(root.val) + '->'
    res_left, res_right = [], []
    if root.right != None:
        res_right = allPaths(root.right, res[:]) #此处res[:]是为了防止列表传址的影响！
    if root.left != None:
        res_left = allPaths(root.left, res[:])
    res = res_left + res_right
    return res

def binaryTreePaths(root):
    res = allPaths(root, [''])
    return res

if __name__ == "__main__":
    nums = [5,2,3,4,7,6,8,9,0]
    root = initTree(nums)
    print(binaryTreePaths(root))
