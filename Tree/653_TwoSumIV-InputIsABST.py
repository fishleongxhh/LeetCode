# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode653: Two Sum IV - Input is a BST问题

from Tree import *

def findTargetCore(root, MySet, k):
    if root:
        if k - root.val in MySet:
            return True
        MySet.add(root.val)
        return findTargetCore(root.left, MySet, k) or findTargetCore(root.right, MySet, k)
    return False

def findTarget(root, k):
    MySet = set()
    return findTargetCore(root, MySet, k)

if __name__ == "__main__":
    nums = [5,3,4,1,2,8,6,7,0,9]
    root = initTree(nums)
    print(nums)
    for k in range(21):
        print(k, findTarget(root, k))
