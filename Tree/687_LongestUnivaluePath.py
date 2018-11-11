# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode687: Longest Univalue Path问题

from Tree import *

#此解法有误，这个函数只能求出从根节点到叶节点的路径上的最长单值子路径的长度
def longestUnivaluePathCore(root, path, curr_len, max_len):
    if root:
        path.append(root.val)
        if len(path) == 1 or path[-1] != path[-2]:
            curr_len.append(0)
        else:
            curr_len.append(curr_len[-1]+1)
        max_len[0] = curr_len[-1] if curr_len[-1] > max_len[0] else max_len[0]
        longestUnivaluePathCore(root.left, path, curr_len, max_len)
        longestUnivaluePathCore(root.right, path, curr_len, max_len)
        path.pop()
        curr_len.pop()

def longestUnivaluePathCore2(root):
    if root:
        leftRes = longestUnivaluePathCore2(root.left)
        rightRes = longestUnivaluePathCore2(root.right)
        if root.val == leftRes[0] and root.val == rightRes[0]:
            maxDiameter = leftRes[2] + rightRes[2] + 2 #经过当前节点的并与当前节点值相同的最大半径
            maxPath = max(leftRes[2], rightRes[2]) + 1 #经过当前节点的并与当前节点值相同的最长路径
        elif root.val == leftRes[0]:
            maxDiameter = leftRes[2] + 1
            maxPath = leftRes[2] + 1
        elif root.val == rightRes[0]:
            maxDiameter = rightRes[2] + 1
            maxPath = rightRes[2] + 1
        else:
            maxDiameter, maxPath = 0, 0
        finalRes = max(leftRes[-1], rightRes[-1], maxDiameter)
        return (root.val, maxDiameter, maxPath, finalRes)
    return (None, -1, -1, 0)

def longestUnivaluePath(root):
    res = longestUnivaluePathCore2(root)
    return res[-1]

if __name__ == "__main__":
    nums = [5,3,3,7,2,1,8,9,0]
    root = initTree(nums)
    print(longestUnivaluePath(root))
