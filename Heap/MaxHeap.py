# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来实现最大堆数据结构及相关操作

class MaxHeap:
    def __init__(self):
        self.size = 0
        self.data = [float('inf')]#最大堆是用数组实现的，0位置出一般放置一个足够大的数

    def isEmpty(self):
        return self.size == 0

    def findMax(self):
        if self.isEmpty():
            #print("The MaxHeap is Empty!")
            return None
        else:
            return self.data[1]

    def insert(self, item):
        self.size += 1
        self.data.append(item)
        curr_loc, next_loc = self.size, self.size//2
        while self.data[next_loc] < item:
            self.data[curr_loc] = self.data[next_loc]
            curr_loc, next_loc = next_loc, next_loc//2
        self.data[curr_loc] = item
    
    #对loc处的元素进行下沉，使其满足堆序性
    def percolateDown(self, loc):
        if loc*2 <= self.size:
            curr_loc, item = loc, self.data[loc]
            next_loc = curr_loc*2 if curr_loc*2+1>self.size or self.data[curr_loc*2+1]<self.data[curr_loc*2] else curr_loc*2+1
            while next_loc <= self.size and item < self.data[next_loc]:
                self.data[curr_loc] = self.data[next_loc]
                curr_loc, next_loc = next_loc, next_loc*2 if next_loc*2+1>self.size or self.data[next_loc*2+1]<self.data[next_loc*2] else next_loc*2+1
            self.data[curr_loc] = item

    def deleteMax(self):
        if self.size == 0:
            #print("The MaxHeap is Empty!")
            pass
        elif self.size == 1:
            self.size -= 1
            self.data.pop()
        else:
            self.data[1] = self.data.pop()
            self.size -= 1
            self.percolateDown(1)

if __name__ == "__main__":
    nums = [5,2,4,6,8,1,7,9,0]
    print(nums)
    obj = MaxHeap()
    for item in nums:
        obj.insert(item)
        print(obj.data)
    while not obj.isEmpty():
        obj.deleteMax()
        print(obj.data)
