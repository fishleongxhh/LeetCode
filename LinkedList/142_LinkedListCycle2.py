# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode142: Linked List Cycle2问题

from LinkedList import *

#找出链表中环的入口节点，如果没有环，则返回None
def detectCycle(head):
    #首先判断是否有环,返回快指针和慢指针首次相遇的节点
    meetNode = hasCycle(head)
    if not meetNode:
        return None
    #再判断环包含的节点个数
    p, cnt = meetNode.nextNode, 1
    while p != meetNode:
        p, cnt = p.nextNode, cnt+1
    #用两个指针确定环的入口位置
    slow = fast = head
    for i in range(cnt):
        fast = fast.nextNode
    while slow != fast:
        slow, fast = slow.nextNode, fast.nextNode
    return slow

def hasCycle(head):
    slow = fast = head
    while fast:
        if fast.nextNode:
            slow, fast = slow.nextNode, fast.nextNode.nextNode
            if slow == fast:
                return slow
        else:
            return None
    return None

if __name__ == "__main__":
    nums = [1]
    headNode = initLinkedList(nums)
    printLinkedList(headNode)
    tailNode = headNode
    """
    while tailNode.nextNode:
        tailNode = tailNode.nextNode
    tailNode.nextNode = headNode
    for i in range(0):
        tailNode.nextNode = tailNode.nextNode.nextNode
    """
    inNode = detectCycle(headNode)
    if inNode:
        print(inNode.val)
    else:
        print(inNode)
