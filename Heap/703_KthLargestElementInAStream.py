# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode703: Kth Largest Element in a Stream问题

class KthLargest:
    def __init__(self, k, nums):
        self.capacity = k #k必须为正整数
        self.size = 0
        self.data = [float('-inf')]
        #根据nums构建堆
        self.buildHeap(nums)
        #如果长度超过k,则进行删除
        while self.size > self.capacity:
            self.deleteMin()

    def add(self, val):
        if self.size < self.capacity:
            self.insert(val)
        else:
            if val > self.data[1]: #这个地方的处理稍显复杂，其实可以直接将val代替self.data[1]，然后使用percolateDown(1)函数对1位置处的元素进行下滤
                self.deleteMin()
                self.insert(val)
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
            print('MinHeap is Empty!')
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
    nums = [8,2]
    k = 4
    print(k, nums)
    obj = KthLargest(k, nums)
    print(obj.data)
    for val in [3,5,10,9,4]:
        print(val, obj.add(val))
    print(obj.data)
