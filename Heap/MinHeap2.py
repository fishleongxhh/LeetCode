# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode378: Kth Smallest Element in a Sorted Matrix问题

#此MinHeap数据结构在上一版上做了改进和简化，也增加了两个函数pushpop和poppush
#同时MinHeap也支持任何可以具有序关系或者定义了序关系的python对象，使用前只需设置好合理的inf_flag即可
class MinHeap:
    def __init__(self, nums = [], inf_flag = float('-inf')):
        self.size = len(nums)
        self.data = [inf_flag] + nums[:]
        for i in range(self.size//2, 0, -1):
            self.__percolateDown(i)

    def __repr__(self):
        print("[" + ",".join([str(item) for item in self.data]) + "]")

    def __str__(self):
        return "[" + ",".join([str(item) for item in self.data]) + "]"

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
            nextLoc = tmpLoc if tmpLoc+1>self.size or self.data[tmpLoc+1] > self.data[tmpLoc] else tmpLoc+1
            if self.data[nextLoc] > self.data[loc]:
                break
            self.data[nextLoc], self.data[loc] = self.data[loc], self.data[nextLoc]
            loc, tmpLoc = nextLoc, nextLoc*2

    def push(self, item):
        self.size += 1
        self.data.append(item)
        #执行上浮操作
        currLoc, nextLoc = self.size, self.size//2
        while self.data[nextLoc] > item:
            self.data[currLoc] = self.data[nextLoc]
            currLoc, nextLoc = nextLoc, nextLoc//2
        self.data[currLoc] = item

    def pop(self):
        if self.size == 0:
            print("MinHeap is Empty!")
        elif self.size == 1:
            self.data.pop()
            self.size -= 1
        else:
            self.data[1] = self.data.pop()
            self.size -= 1
            self.__percolateDown(1)

    def pushpop(self, item):
        if self.size == 0:
            return item
        currMin = self.findMin()
        if item < currMin:
            return item
        else:
            self.data[1] = item
            self.__percolateDown(1)
            return currMin

    def poppush(self, item):
        if self.size == 0:
            print("MinHeap is Empty!")
            return None
        currMin = self.findMin()
        self.data[1] = item
        self.__percolateDown(1)
        return currMin

