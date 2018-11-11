# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode237: Delete Node in a Linked List问题

from LinkedList import *

#使用平均复杂度为O(1)的算法删除链表节点
#必须假定节点一定在链表中，否则需要O(n)时间来进行检验
#如果仅用来解决237问题，则该节点也一定不是尾节点，这样算法会简化
def deleteNode(headNode, node):
    tmpNode = node.nextNode
    #如果node不是尾节点
    if tmpNode:
        node.val, node.nextNode = tmpNode.val, tmpNode.nextNode
    #如果node是尾节点，那么就需要顺序查找，然后删除
    else:
        headNode = deleteNodeByOrder(headNode, node)
    return headNode

#此函数使用顺序查找删除尾节点，时间复杂度为O(n)
#这里的node必须为尾节点！！
def deleteNodeByOrder(headNode, node):
    #如果仅有一个节点，且是该尾节点，则返回空
    if headNode == node:
        return None
    currNode = headNode
    while currNode.nextNode != node:
        currNode = currNode.nextNode
    currNode.nextNode = None
    return headNode

if __name__ == "__main__":
    nums = [1]
    headNode = initLinkedList(nums)
    printLinkedList(headNode)
    newNode = deleteNode(headNode, headNode)
    printLinkedList(newNode)
