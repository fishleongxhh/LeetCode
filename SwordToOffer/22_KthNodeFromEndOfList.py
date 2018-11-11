# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解剑指offer22: 求链表倒数第K个节点

from LinkedList import *

#k必须为正整数
def KthFromEnd(head, k):
    #首先，如果head为空，或者k不是正整数，则返回空
    if (not head) or k <= 0:
        return None
    p = q = head
    #首先将q前进k步，如果发现链表长度不足k，则返回None
    while k > 0:
        q, k = q.nextNode, k-1
        if (not q) and k > 0:
            return None
    while q:
        p, q = p.nextNode, q.nextNode
    return p

if __name__ == "__main__":
    nums = []
    k = 1
    headNode = initLinkedList(nums)
    printLinkedList(headNode)
    print(k)
    node = KthFromEnd(headNode, k)
    if node:
        print(node.val)
    else:
        print(node)
