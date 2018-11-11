# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode82: Remove Duplicates from Sorted List2问题

from LinkedList import *

#注意，头节点也有可能被删除！仅保留那些只出现一次的节点
def deleteDuplicates(head):
    #考虑到头节点可能会被删除，因此先新建一个新的头节点
    newHead = ListNode(float('inf'))
    newHead.nextNode, currNode = head, head
    tmpNode = newHead
    while currNode:
        if not currNode.nextNode:
            break
        if currNode.val != currNode.nextNode.val:
            tmpNode.nextNode, currNode = currNode, currNode.nextNode
            tmpNode = tmpNode.nextNode
        flag = False #用来标记是否出现重复
        while currNode.nextNode and currNode.val == currNode.nextNode.val:
            currNode = currNode.nextNode
            flag = True
        if flag:
            currNode = currNode.nextNode
    tmpNode.nextNode = currNode
    return newHead.nextNode

if __name__ == "__main__":
    nums = []
    headNode = initLinkedList(nums)
    printLinkedList(headNode)
    newHead = deleteDuplicates(headNode)
    printLinkedList(newHead)
