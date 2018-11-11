# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序主要涉及到二叉树的一些基本操作
# 定义二叉树，初始化二叉查找树，先序、中序、后序遍历二叉树

class TreeNode:
    def __init__ (self, x):
        self.val = x
        self.left = None
        self.right = None

#按照元素顺序，将其初始化为一个二叉查找树
def initTree(nums):
    if not nums:
        return None
    rootNode = TreeNode(nums[0])
    for item in nums[1:]:
        currNode = TreeNode(item)
        tmpNode = rootNode
        while True:
            if item <= tmpNode.val:
                if tmpNode.left == None:
                    tmpNode.left = currNode
                    break
                else:
                    tmpNode = tmpNode.left
            else:
                if tmpNode.right == None:
                    tmpNode.right = currNode
                    break
                else:
                    tmpNode = tmpNode.right
    return rootNode

#中序遍历+先序遍历，或者中序遍历+后序遍历都可以唯一确定一棵二叉树，但是先序+后序不行
#先序遍历二叉树
def preOrderScan(rootNode, res=''):
    if rootNode == None:
        return res + ''
    res = preOrderScan(rootNode.left, res)
    res = res + '->' + str(rootNode.val)
    res = preOrderScan(rootNode.right, res)
    return res

def midOrderScan(rootNode, res=''):
    if rootNode == None:
        return res + ''
    res = res + '->' + str(rootNode.val)
    res = midOrderScan(rootNode.left, res)
    res = midOrderScan(rootNode.right, res)
    return res

def postOrderScan(rootNode, res=''):
    if rootNode == None:
        return res + ''
    res = postOrderScan(rootNode.left, res)
    res = postOrderScan(rootNode.right, res)
    res = res + '->' + str(rootNode.val)
    return res

def treeScan(rootNode):
    print("先序遍历")
    print(preOrderScan(rootNode))
    print("中序遍历")
    print(midOrderScan(rootNode))
    print("后序遍历")
    print(postOrderScan(rootNode))

if __name__ == "__main__":
    nums1 = [5,1,3,2,7,9,8]
    print(nums1)
    rootNode1 = initTree(nums1)
    treeScan(rootNode1)

