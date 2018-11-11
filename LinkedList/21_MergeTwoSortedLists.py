# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode21: Merge Two Sorted Lists问题

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

def mergeTwoLists(l1, l2):
    HeadNode = CurrNode = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            CurrNode.nextNode = l1
            l1 = l1.nextNode
        else:
            CurrNode.nextNode = l2
            l2 = l2.nextNode
        CurrNode = CurrNode.nextNode
    CurrNode.nextNode = (l1 or l2)
    return HeadNode.nextNode

if __name__ == "__main__":
    nums1 = [1,3,5,7]
    nums2 = [1,3,4]
    l1 = initListNode(nums1)
    l2 = initListNode(nums2)
    printListNode(l1)
    printListNode(l2)
    l = mergeTwoLists(l1, l2)
    printListNode(l)
