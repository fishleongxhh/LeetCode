# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode160: Intersection of Two Linked Lists问题

class ListNode():
    def __init__(self, x):
        self.val = x
        self.nextNode = None

def initLinkedList(nums):
    HeadNode = ListNode(0)
    CurrNode = HeadNode
    for item in nums:
        TmpNode = ListNode(item)
        CurrNode.nextNode, CurrNode = TmpNode, TmpNode
    return HeadNode.nextNode

def printLinkedList(HeadNode):
    res = ''
    while HeadNode != None:
        res = res + str(HeadNode.val) + '->'
        HeadNode = HeadNode.nextNode
    print(res)

def getIntersectionNode(headA, headB):
    if headA == None or headB == None:
        return None
    #先计算两条链表的长度差
    currA, currB = headA, headB
    flag = 0
    while flag < 2:
        if currA.nextNode == None:
            currA, flag = headB, flag+1
        else:
            currA = currA.nextNode
        if currB.nextNode == None:
            currB, flag = headA, flag+1
        else:
            currB = currB.nextNode
    #循环结束后，currA正在链表B上，currB正在链表A上，且较长的那个链上的指针要多走几步
    #两个指针同步往前走，只记录上一次不相等的节点
    TagNode, StartNode = None, currA
    while currA != None:
        if currA != currB:
            TagNode = currA
        currA, currB = currA.nextNode, currB.nextNode
    if TagNode == None:
        return StartNode
    else:
        return TagNode.nextNode

#LeetCode上的一个非常简洁漂亮的答案！！
def getIntersectionNode2(headA, headB):
    if headA is None or headB is None:
        return None
    pa = headA
    pb = headB
    while pa is not pb:
        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next
    return pa

if __name__ == "__main__":
    nums1 = [1,2,3]
    l1 = initLinkedList(nums1)
    nums2 = []
    l2 = l1
    #l2 = initLinkedList(nums2)
    common = initLinkedList([1,2,3,4])
    l1.nextNode = common
    l2.nextNode = common
    printLinkedList(l1)
    printLinkedList(l2)
    printLinkedList(getIntersectionNode2(l1,l2))
