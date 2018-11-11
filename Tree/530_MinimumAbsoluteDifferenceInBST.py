# -*- coding: utf -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode530: Minimum Absolute Difference in BST问题


from Tree import *

def preOrderTraversal(root, res):
    if root:
        preOrderTraversal(root.left, res)
        res.append(root.val)
        preOrderTraversal(root.right, res)

def getMinimumDifference(root):
    res = []
    preOrderTraversal(root, res)
    if len(res) >= 2:
        return min((res[i]-res[i-1] for i in range(1,len(res))))
    return None

if __name__ == "__main__":
    nums = [5,3,8]
    print(nums)
    root = initTree(nums)
    print(getMinimumDifference(root))
