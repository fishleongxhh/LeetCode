# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode637: Average of Levels in Binary Tree问题

from Tree import *

def levelOrder(root, res, level):
    if root:
        if len(res) < level:
            res.append([root.val])
        else:
            res[level-1].append(root.val)
        levelOrder(root.left, res, level+1)
        levelOrder(root.right, res, level+1)

#root一定是非空的
def averageOfLevels(root):
    res = [] #记录层次遍历的结果
    levelOrder(root, res, 1)
    return [sum(l)/len(l) for l in res]

if __name__ == "__main__":
    root = initTree([])
    print(averageOfLevels(root))
