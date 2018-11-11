# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来确定一个节点在一棵普通二叉树中的搜索路径

from Tree import *

#注意，node必须要在root中出现过，且root树中节点都是唯一的
def searchTree(root, path, node):
    if root:
        path.append(root)
        if root.val == node.val:
            return True
        flag = searchTree(root.left, path, node)
        if flag:
            return flag
        flag = searchTree(root.right, path, node)
        if flag:
            return flag
        path.pop()
        return False
    return False

if __name__ == "__main__":
    nums = [5,1,3,2,7,9,8]
    print(nums)
    root = initTree(nums)
    node = TreeNode(7)
    path = []
    if searchTree(root, path, node):
        for item in path:
            print(item.val)
