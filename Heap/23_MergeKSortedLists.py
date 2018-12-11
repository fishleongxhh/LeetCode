# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来解决LeetCode23. Merge k Sorted Lists问题

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class MinHeap:
    def __init__(self, nums = [], inf_flag = ListNode(float('-inf'))):
        self.size = len(nums)
        self.data = [inf_flag] + nums[:]
        for i in range(self.size//2, 0, -1):
            self.__percolateDown(i)

    def isEmpty(self):
        return self.size == 0

    def findMin(self):
        if self.size == 0:
            print("MinHeap is Empty!")
            return None
        else:
            return self.data[1]
    
    #对loc位置执行下沉操作
    def __percolateDown(self, loc):
        tmpLoc = loc*2
        while tmpLoc <= self.size:
            nextLoc = tmpLoc if tmpLoc+1>self.size or self.data[tmpLoc+1].val > self.data[tmpLoc].val else tmpLoc+1
            if self.data[nextLoc].val > self.data[loc].val:
                break
            self.data[nextLoc], self.data[loc] = self.data[loc], self.data[nextLoc]
            loc, tmpLoc = nextLoc, nextLoc*2

    def pop(self):
        if self.size == 0:
            res = None
        elif self.size == 1:
            res = self.data.pop()
            self.size -= 1
        else:
            res = self.data[1]
            self.data[1] = self.data.pop()
            self.size -= 1
            self.__percolateDown(1)
        return res

    def poppush(self, item):
        if self.size == 0:
            print("MinHeap is Empty!")
            return None
        currMin = self.findMin()
        self.data[1] = item
        self.__percolateDown(1)
        return currMin

def mergeKLists(lists):
    lists = [item for item in lists if item] #将None过滤掉
    if not lists:
        return None
    MyMinHeap = MinHeap(lists)
    root = curr = ListNode(0)
    while not MyMinHeap.isEmpty():
        while (not MyMinHeap.isEmpty()) and (not MyMinHeap.findMin().next):
            curr.next = MyMinHeap.pop()
            curr = curr.next
        if not MyMinHeap.isEmpty():
            curr.next = MyMinHeap.poppush(MyMinHeap.findMin().next)
            curr = curr.next
    return root.next

if __name__ == "__main__":
    lists = [ListNode(3), ListNode(1), ListNode(2)]
    res = mergeKLists(lists)
    while res:
        print(res.val)
        res = res.next
