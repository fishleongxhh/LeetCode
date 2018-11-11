# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来定义链表的数据结构以及初始化和打印操作

class ListNode():
    def __init__(self, x):
        self.val = x
        self.nextNode = None

def initLinkedList(nums):
    headNode = ListNode(0)
    prevNode = headNode
    for item in nums:
        currNode = ListNode(item)
        prevNode.nextNode, prevNode = currNode, currNode
    return headNode.nextNode

def printLinkedList(headNode):
    res = ''
    while headNode:
        res = res + str(headNode.val) + '->'
        headNode = headNode.nextNode
    print(res)
