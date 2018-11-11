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

def hasCycle(head):
    if not head:
        return False
    Node1 = Node2 = head
    while Node1 and Node2:
        if (not Node1.nextNode) or (not Node2.nextNode) or (not Node2.nextNode.nextNode):
            return False
        Node1, Node2 = Node1.nextNode, Node2.nextNode.nextNode
        if Node1 == Node2:
            return True
    return False

if __name__ == "__main__":
    nums1 = [1,2,3,4]
    l1 = initListNode(nums1)
    printListNode(l1)
    flag = hasCycle(l1)
    print(flag)
