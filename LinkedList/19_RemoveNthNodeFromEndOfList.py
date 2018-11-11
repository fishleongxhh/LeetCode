# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode19: Remove Nth Node From End of List问题

from LinkedList import *

def removeNthFromEnd(head, n):
    if (not head) or n <= 0:
        return head
    #先创建一个新的头节点
    newHead = ListNode(0)
    newHead.nextNode = head
    p, q = newHead, head
    #如果链表节点个数不足n，则返回head
    while n > 0:
        q, n = q.nextNode, n-1
        if (not q) and n > 0:
            return head
    while q:
        p, q = p.nextNode, q.nextNode
    #此时删除p的下一个节点
    p.nextNode = p.nextNode.nextNode
    return newHead.nextNode

if __name__ == "__main__":
    nums = []
    headNode = initLinkedList(nums)
    printLinkedList(headNode)
    n = 1
    print(n)
    printLinkedList(removeNthFromEnd(headNode,n))
