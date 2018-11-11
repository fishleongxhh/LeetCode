# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode106: Construct Binary Tree from Inorder and Postorder Traversal问题

from Tree import *

def buildTreeCore(inorder, postorder, startIn, endIn, startPost, endPost):
    if startIn > endIn or startPost > endPost:
        return None
    rootVal = postorder[endPost]
    for rootLoc in range(startIn, endIn+1):
        if inorder[rootLoc] == rootVal:
            break
    if rootLoc == endIn and inorder[rootLoc] != rootVal:
        print("Invalid Input!")
        return None
    rootNode = TreeNode(rootVal)
    rootNode.left = buildTreeCore(inorder, postorder, startIn, rootLoc-1, startPost, startPost+rootLoc-1-startIn)
    rootNode.right = buildTreeCore(inorder, postorder, rootLoc+1, endIn, rootLoc+endPost-endIn, endPost-1)
    return rootNode

def buildTree(inorder, postorder):
    if len(inorder) != len(postorder):
        print("Invalid Input!")
        return None
    if (not inorder) or (not postorder):
        return None
    rootNode = buildTreeCore(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
    return rootNode

if __name__ == "__main__":
    inorder = []
    postorder = []
    print(inorder)
    print(postorder)
    rootNode = buildTree(inorder, postorder)
    print(preOrderScan(rootNode))
    print(postOrderScan(rootNode))
