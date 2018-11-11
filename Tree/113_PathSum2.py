# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode113: Path Sum 2问题

from Tree import *

def pathSumCore(root, target, path, res):
    if root:
        path.append(root.val)
        if (not root.left) and (not root.right):
            if root.val == target:
                res.append(path[:])
        if root.left:
            pathSumCore(root.left, target-root.val, path, res)
        if root.right:
            pathSumCore(root.right, target-root.val, path, res)
        path.pop()

def pathSum(root, sum):
    path, res = [], []
    pathSumCore(root, sum, path, res)
    return res

if __name__ == "__main__":
    nums = [5,3,8,2,4,7,9,0,6,1]
    root = initTree(nums)
    res = pathSum(root, 11)
    for path in res:
        print(path)
