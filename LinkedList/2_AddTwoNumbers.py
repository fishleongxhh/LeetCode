# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode2: Add Two Numbers问题

from LinkedList import *

#没有对l1或l2进行修改，因此运行会慢一点，我们也可以对l1或l2进行修改，这样会快很多
def addTwoNumbers(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    spill = 0
    currNode = headNode = ListNode(0)
    while l1 or l2:
        value = spill
        if l1:
            value += l1.val
            l1 = l1.nextNode
        if l2:
            value += l2.val
            l2 = l2.nextNode
        currNode.nextNode = ListNode(value%10)
        currNode = currNode.nextNode
        spill = value//10
    if spill:
        currNode.nextNode = ListNode(spill)
    return headNode.nextNode

if __name__ == "__main__":
    n1, n2 = 10, 0
    l1 = initLinkedList([int(item) for item in list(str(n1))[::-1]])
    l2 = initLinkedList([int(item) for item in list(str(n2))[::-1]])
    l = addTwoNumbers(l1, l2)
    printLinkedList(l)
    print(str(n1+n2)[::-1])
