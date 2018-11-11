# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode617: Merge Two Binary Trees问题

from Tree import *

#对原始的树没有做修改，新建了一棵树，速度会慢一点
def mergeTrees(t1,t2):
    if (not t1) and (not t2):
        root = None
    elif not t1:
        root = TreeNode(t2.val)
        root.left = mergeTrees(t1, t2.left)
        root.right = mergeTrees(t1, t2.right)
    elif not t2:
        root = TreeNode(t1.val)
        root.left = mergeTrees(t1.left, t2)
        root.right = mergeTrees(t1.right, t2)
    else:
        root = TreeNode(t1.val+t2.val)
        root.left = mergeTrees(t1.left, t2.left)
        root.right = mergeTrees(t1.right, t2.right)
    return root

#也可以对原始树做修改，这样速度会快很多
def mergeTrees2(t1,t2):
    if (not t1) and (not t2):
        return None
    elif not t1:
        return t2
    elif not t2:
        return t1
    else:
        t1.val += t2.val
        t1.left = mergeTrees2(t1.left, t2.left)
        t1.right = mergeTrees2(t1.right, t2.right)
        return t1

if __name__ == "__main__":
    t1 = initTree([10,4,6,2,7,9,12,13,15,17,14])
    t2 = initTree([15,2,5,8,23,18,19,0])
    t = mergeTrees2(t1,t2)
    print(preOrderScan(t))
