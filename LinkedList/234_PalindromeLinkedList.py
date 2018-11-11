# -*- coding: utf-8 -*-
# Author: Xu Hanhui
#此程序用来求解LeetCode234: Palindrome Linked List回文链表问题

class ListNode():
    def __init__(self,x):
        self.val = x
        self.nextNode = None

def initLinkedList(nums):
    HeadNode = CurrNode = ListNode(0)
    for item in nums:
        NewNode = ListNode(item)
        CurrNode.nextNode = NewNode
        CurrNode = NewNode
    return HeadNode.nextNode

def printLinkedList(HeadNode):
    res = ''
    while HeadNode != None:
        res = res + str(HeadNode.val) + '->'
        HeadNode = HeadNode.nextNode
    print(res)

def isPalindrome(head):
    #无节点或者只有一个节点
    if head == None or head.nextNode == None:
        return True
    #找到链表的中点
    SlowNode, FastNode = head, head
    while FastNode.nextNode != None and FastNode.nextNode.nextNode != None:
        SlowNode = SlowNode.nextNode
        FastNode = FastNode.nextNode.nextNode
    MidNode = SlowNode.nextNode
    #将链表的后半部分反转
    CurrNode, NextNode = MidNode, MidNode.nextNode
    while NextNode != None:
        TmpNode = NextNode.nextNode
        NextNode.nextNode = CurrNode
        CurrNode, NextNode = NextNode, TmpNode
    MidNode.nextNode = None
    #对比前半条和后半条链表是否相同
    while CurrNode != None:
        if CurrNode.val != head.val:
            return False
        CurrNode, head = CurrNode.nextNode, head.nextNode
    return True

if __name__ == "__main__":
    nums1 = [1,2,3,4,5,5,4,3,2,1]
    l1 = initLinkedList(nums1)
    printLinkedList(l1)
    print(isPalindrome(l1))
