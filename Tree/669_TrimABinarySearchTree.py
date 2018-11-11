# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode669: Trim a Binary Search Tree问题

from Tree import *

def trimBST(root, L, R):
    if root:
        if root.val >= L and root.val <= R:
            root.left = trimBST(root.left, L, R)
            root.right = trimBST(root.right, L, R)
            return root
        elif root.val < L:
            while root and root.val < L:
                root = root.right
            return trimBST(root, L, R)
        else:
            while root and root.val > R:
                root = root.left
            return trimBST(root, L, R)
    return None

if __name__ == "__main__":
    nums = []
    root = initTree(nums)
    print(preOrderScan(root))
    L, R = 1, 2
    root = trimBST(root, L, R)
    print(L, R)
    print(preOrderScan(root))
