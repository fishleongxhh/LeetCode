# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode141: Linked List Cycle问题

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

def removeElements(head, val):
    #为了逻辑简便，引入一个头节点
    HeadNode = ListNode(0)
    HeadNode.nextNode = head
    #两个指针，一个是当前节点，一个是下一个节点
    CurrNode, NextNode = HeadNode, HeadNode.nextNode
    while NextNode:
        if NextNode.val == val:
            NextNode = NextNode.nextNode
            CurrNode.nextNode = NextNode
        else:
            CurrNode, NextNode = NextNode, NextNode.nextNode
    return HeadNode.nextNode

if __name__ == "__main__":
    nums1 = [2]
    l1 = initListNode(nums1)
    printListNode(l1)
    l1 = removeElements(l1, 1)
    printListNode(l1)
