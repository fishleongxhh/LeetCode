# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode572: Subtree of Another Tree问题

from Tree import *
from BinaryTreeLevelOrderTraversal import *

def isSubtree(s,t):
    if not t:
        return True
    if not s:
        return False
    if s.val != t.val:
        flag = isSubtree(s.left, t) or isSubtree(s.right, t)
    else:
        flag = check(s,t) or isSubtree(s.left, t) or isSubtree(s.right, t)
    return flag

#用于判断两棵树是否相同
def check(s,t):
    if (not s) and (not t):
        return True
    if (not s) or (not t) or (s.val != t.val):
        return False
    flag = check(s.left, t.left) and check(s.right, t.right)
    return flag

if __name__ == "__main__":
    nums = [5,1,4,7,8,9,2,0,6]
    rootNode = initTree(nums)
    print(levelOrderBottom(rootNode))
    root2 = initTree([5,1,7])
    print(midOrderScan(rootNode))
    print(midOrderScan(root2))
    print(isSubtree(rootNode,root2))
