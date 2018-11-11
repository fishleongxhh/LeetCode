# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode295: Find Median from Data Stream问题

from MinHeap import MinHeap
from MaxHeap import MaxHeap

class MedianFinder(object):

    def __init__(self):
        self.cnt = 0
        self.LeftMaxHeap = MaxHeap()
        self.RightMinHeap = MinHeap()

    def addNum(self, num):
        self.cnt += 1
        if self.cnt % 2:
            if (not self.RightMinHeap.isEmpty()) and self.RightMinHeap.findMin() < num:
                self.RightMinHeap.insert(num)
                self.LeftMaxHeap.insert(self.RightMinHeap.findMin())
                self.RightMinHeap.deleteMin()
            else:
                self.LeftMaxHeap.insert(num)
        else:
            if (not self.LeftMaxHeap.isEmpty()) and self.LeftMaxHeap.findMax() > num:
                self.LeftMaxHeap.insert(num)
                self.RightMinHeap.insert(self.LeftMaxHeap.findMax())
                self.LeftMaxHeap.deleteMax()
            else:
                self.RightMinHeap.insert(num)

    def findMedian(self):
        if self.cnt == 0:
            return None
        else:
            if self.cnt % 2:
                return float(self.LeftMaxHeap.findMax())
            else:
                return (self.LeftMaxHeap.findMax() + self.RightMinHeap.findMin())/2

if __name__ == "__main__":
    obj = MedianFinder()
    nums = [1,2,3]
    print(nums)
    for item in nums:
        obj.addNum(item)
        print(obj.LeftMaxHeap.data, obj.RightMinHeap.data)
        print(obj.findMedian())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
