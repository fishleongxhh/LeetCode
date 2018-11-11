# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序主要实现最小堆的数据结构和基本操作

class MinHeap:
    def __init__(self):
        self.size = 0
        self.data = [float('-inf')] #最小堆数组的第一个位置一般放一个标志元素，这个元素比所有可能的元素都要小

    def isEmpty(self):
        return self.size == 0

    def findMin(self):
        if self.size == 0:
            #print("MinHeap is Empty!")
            return None
        return self.data[1]

    def insert(self, x):
        self.data.append(x)
        curr_loc = self.size = self.size + 1
        while self.data[curr_loc//2] > x:
            self.data[curr_loc] = self.data[curr_loc//2]
            curr_loc //= 2
        self.data[curr_loc] = x

    def deleteMin(self):
        if self.size == 0:
            #print('MinHeap is Empty!')
            pass
        elif self.size == 1:
            self.data.pop()
            self.size -= 1
        else:
            curr_loc, item = 1, self.data[-1]
            self.data.pop()
            self.size -= 1
            tmp_loc = 2*curr_loc
            next_loc = tmp_loc if (self.size <= tmp_loc or self.data[tmp_loc] < self.data[tmp_loc+1]) else tmp_loc+1
            while next_loc <= self.size and self.data[next_loc] < item:
                self.data[curr_loc] = self.data[next_loc]
                curr_loc, tmp_loc= next_loc, 2*next_loc
                next_loc = tmp_loc if (self.size <= tmp_loc or self.data[tmp_loc] < self.data[tmp_loc+1]) else tmp_loc+1
            self.data[curr_loc] = item
    #此函数用来判断第loc个位置的元素是否满足堆序性，若不满足，则下沉.此函数暂时只用于初始化构建堆
    def percolateDown(self, loc):
        if loc*2 <= self.size:
            curr_loc, tmp_loc = loc, 2*loc
            next_loc = tmp_loc if (self.size <= tmp_loc or self.data[tmp_loc] < self.data[tmp_loc+1]) else tmp_loc+1
            while next_loc <= self.size and self.data[curr_loc] > self.data[next_loc]:
                self.data[next_loc], self.data[curr_loc] = self.data[curr_loc], self.data[next_loc]
                curr_loc, tmp_loc = next_loc, 2*next_loc
                next_loc = tmp_loc if (self.size <= tmp_loc or self.data[tmp_loc] < self.data[tmp_loc+1]) else tmp_loc+1
    #根据一个list来初始化构建一个最小堆
    def buildHeap(self, data_list): 
        self.size = len(data_list)
        self.data.extend(data_list[:])
        for i in range(self.size//2, 0, -1):
            self.percolateDown(i)

if __name__ == "__main__":
    obj = MinHeap()
    """
    data = []
    print(data)
    for item in data:
        obj.insert(item)
    print(obj.data)
    for i in range(len(data)+1):
        print(obj.findMin())
        print(obj.data)
        obj.deleteMin()
    """
    data = [6,4,5,7,3]
    print(data)
    obj.buildHeap(data)
    print(obj.data)
