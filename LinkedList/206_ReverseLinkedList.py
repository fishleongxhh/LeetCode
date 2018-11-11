# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode206: Reverse Linked List问题

class ListNode:
    def __init__(self,x):
        self.val = x
        self.nextNode = None

def initListNode(nums):
    if not nums:
        return None
    CurrNode = HeadNode = ListNode(nums[0])
    for val in nums[1:]:
        NextNode = ListNode(val)
        CurrNode.nextNode = NextNode
        CurrNode = NextNode
    return HeadNode

def printListNode(StartNode):
    res = ""
    while StartNode:
        res = res + str(StartNode.val) + "->"
        StartNode = StartNode.nextNode
    print(res)

def reverseList(head):
    if not head:
        return head
    CurrNode, NextNode = head, head.nextNode
    while NextNode:
        TmpNode = NextNode
        NextNode = NextNode.nextNode
        TmpNode.nextNode, CurrNode = CurrNode, TmpNode
    head.nextNode = None #这一句很重要！第一个节点变成最后一个节点！
    return CurrNode

if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,7,8,9]
    l1 = initListNode(nums1)
    printListNode(l1)
    l1 = reverseList(l1)
    printListNode(l1)
