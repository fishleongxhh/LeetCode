# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode83: Remove Duplicates from Sorted List问题

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

def deleteDuplicates(HeadNode):
    if HeadNode:
        PrevNode, CurrNode = HeadNode, HeadNode.nextNode
        PrevNode.nextNode = None #这一步很重要！！
        while CurrNode:
            if CurrNode.val != PrevNode.val:
                PrevNode.nextNode = CurrNode
                PrevNode, CurrNode = CurrNode, CurrNode.nextNode
                PrevNode.nextNode=None #这一步很重要，且不能前置！！
            else:
                CurrNode = CurrNode.nextNode
    return HeadNode

if __name__ == "__main__":
    nums1 = [1,1]
    l1 = initListNode(nums1)
    printListNode(l1)
    l1 = deleteDuplicates(l1)
    printListNode(l1)
