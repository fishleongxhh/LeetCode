# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode876: Middle of the Linked List问题

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

#给定的链表节点数至少为1
def middleNode(head):
    if head == None:
        return head
    node1 = node2 = head
    while node2:
        if node2.nextNode == None:
            return node1
        if node2.nextNode.nextNode == None:
            return node1.nextNode
        node1, node2 = node1.nextNode, node2.nextNode.nextNode

if __name__ == "__main__":
    nums1 = [1,2,3,4]
    l1 = initListNode(nums1)
    printListNode(l1)
    l2 = middleNode(l1)
    printListNode(l2)
