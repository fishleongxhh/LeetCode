# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode112: Path Sum问题

from Tree import TreeNode
from Tree import initTree

def hasPathSum(root, sum):
    if not root:
        return False
    if (not root.left) and (not root.right):
        return root.val == sum
    if not root.left:
        return hasPathSum(root.right, sum-root.val)
    if not root.right:
        return hasPathSum(root.left, sum-root.val)
    return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum-root.val)

#下面的函数将和为某值的所有路径都打印出来
def allPathSum(root, mySum, res, path):
    if root:
        path.append(str(root.val))
        if (not root.left) and (not root.right):
            if mySum == root.val:
                res.append('->'.join(path))
        if root.left:
            allPathSum(root.left, mySum-root.val, res, path)
        if root.right:
            allPathSum(root.right, mySum-root.val, res, path)
        path.pop()

if __name__ == "__main__":
    nums = [10,5,12,4,7,3]
    mySum = 22
    print(nums)
    root = initTree(nums)
    print(hasPathSum(root,mySum))
    res, path = [], []
    allPathSum(root, mySum, res, path)
    for item in res:
        print(item)
