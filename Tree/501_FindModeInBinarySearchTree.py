# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode501: Find Mode in Binary Search Tree问题

from Tree import TreeNode, initTree, treeScan

#max_cnt = 0

def findModeKernel(root, dic, max_cnt):
    if root:
        dic[root.val] = dic.get(root.val, 0) + 1
        max_cnt = max(max_cnt, dic[root.val])
        max_cnt = findModeKernel(root.left, dic, max_cnt)
        max_cnt = findModeKernel(root.right, dic, max_cnt)
    return max_cnt

def findMode(root):
    dic, res = {}, []
    max_cnt = findModeKernel(root, dic, 0)
    for key,cnt in dic.items():
        if cnt == max_cnt:
            res.append(key)
    return res

if __name__ == "__main__":
    nums = [5,2,7,5]
    root = initTree(nums)
    print(nums)
    treeScan(root)
    print(findMode(root))
