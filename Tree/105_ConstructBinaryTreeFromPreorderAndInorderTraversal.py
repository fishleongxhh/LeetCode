# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode105: Construct Binary Tree from Preorder and Inorder Traversal问题

from Tree import *

def buildTree(preorder, inorder):
    if (not preorder) or (not inorder) or (len(preorder) != len(inorder)):
        return None
    rootNode = buildCore(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
    return rootNode

def buildCore(preorder, inorder, startPre, endPre, startIn, endIn):
    if startPre > endPre or startIn > endIn:
        return None
    rootVal = preorder[startPre]
    for rootLoc in range(startIn, endIn+1):
        if inorder[rootLoc] == rootVal:
            break
    if rootLoc == endIn and inorder[rootLoc] != rootVal:
        print("Invalid Input!")
        return None
    rootNode = TreeNode(rootVal)
    rootNode.left = buildCore(preorder, inorder, startPre+1, startPre+rootLoc-startIn, startIn, rootLoc-1)
    rootNode.right = buildCore(preorder, inorder, startPre+rootLoc-startIn+1, endPre, rootLoc+1, endIn)
    return rootNode

if __name__ == "__main__":
    preorder = [3,4,5,6,7]
    inorder = [3,4,5,6,7]
    print(preorder)
    print(inorder)
    rootNode = buildTree(preorder, inorder)
    print(midOrderScan(rootNode))
    print(preOrderScan(rootNode))
