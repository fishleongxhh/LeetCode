# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode102: BinaryTreeLevelOrderTraversal问题

from Tree import *

def levelOrderCore(root, res, level):
    if root:
        if len(res) < level:
            res.append([root.val])
        else:
            res[level-1].append(root.val)
        levelOrderCore(root.left, res, level+1)
        levelOrderCore(root.right, res, level+1)

def levelOrder(root):
    res = []
    levelOrderCore(root, res, 1)
    return res

if __name__ == "__main__":
    nums = []
    root = initTree(nums)
    res = levelOrder(root)
    for row in res:
        print(row)
