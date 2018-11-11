# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode111: Minimum Depth of Binary Tree问题

from Tree import TreeNode
from Tree import initTree

def minDepth(root):
    if not root:
        return 0
    #注意，要考虑到，路径必须是通向叶节点的！！！
    left_depth, right_depth = minDepth(root.left), minDepth(root.right)
    if min(left_depth, right_depth) == 0:
        return max(left_depth, right_depth) + 1
    return min(left_depth, right_depth) + 1

if __name__ == "__main__":
    nums = [5,2,3,1,4,8,6,7,9,0]
    #nums = []
    print(nums)
    root = initTree(nums)
    print(minDepth(root))
