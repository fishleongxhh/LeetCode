# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode235: Lowest Common Ancestor of a Binary Search Tree问题

from Tree import TreeNode
from Tree import initTree

#root树中的元素都是唯一的，无重复值
#node一定是root中的一个节点，否则不能输出正确路径
def searchPath(root, node, path):
    if root:
        path.append(root)
        if root.val > node.val:    
            searchPath(root.left, node, path)
        if root.val < node.val:
            searchPath(root.right, node, path)

def lowestCommonAncestor(root, p, q):
    path_p, path_q = [], []
    searchPath(root, p, path_p)
    searchPath(root, q, path_q)
    for i in range(min(len(path_p),len(path_q))):
        if path_p[i] != path_q[i]:
            return path_p[i-1]
    #最后这一句很重要！！不能丢！！
    return path_p[i]

if __name__ == "__main__":
    nums = [5,2,3,1,4,8,6,7,9,0]
    root = initTree(nums)
    path = []
    node = TreeNode(7)
    searchPath(root, node, path)
    print([item.val for item in path])
    print(lowestCommonAncestor(root, TreeNode(7), TreeNode(4)).val)
