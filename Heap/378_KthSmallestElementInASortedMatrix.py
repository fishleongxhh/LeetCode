# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode378: Kth Smallest Element in a Sorted Matrix问题

class Item:
    def __init__(self, val, iloc, jloc):
        self.val, self.iloc, self.jloc = val, iloc, jloc
    
    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val
    
    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __repr__(self):
        return "Item({},{},{})".format(self.val, self.iloc, self.jloc)

    def __str__(self):
        return "Item({},{},{})".format(self.val, self.iloc, self.jloc)

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

#使用最小堆，计算排序矩阵中第K小的数，如果数字相同，序也要累加
def kthSmallest(matrix, k):
    if not matrix:
        return None
    if not matrix[0]:
        return None
    m, n = len(matrix), len(matrix[0])
    if m*n < k:
        return None
    MyMinHeap = MinHeap([Item(matrix[i][0],i,0) for i in range(m)], inf_flag = Item(float('-inf'),-1,-1))
    res, cnt = Item(float('-inf'),-1,-1), 0
    while cnt < k:
        res, cnt = MyMinHeap.findMin(), cnt+1
        MyMinHeap.pop()
        if res.jloc < n-1:
            MyMinHeap.push(Item(matrix[res.iloc][res.jloc+1], res.iloc, res.jloc+1))
    return res.val

#在一个升序数组中找小于或者等于一个数的元素的数目
def countListLessEqual(nums, target):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] <= target: #如果只想计算小于target的元素数目，则此处改成<号
            start = mid + 1
        else:
            end = mid - 1
    return start

#在一个每行都是升序数组的矩阵中找小于等于一个数的元素的数目
def countMatrixLeassEqual(matrix, target):
    cnt = 0
    for i in range(len(matrix)):
        cnt += countListLessEqual(matrix[i], target)
    return cnt

#使用二分法，计算排序矩阵中第K小的数，如果数字相同，序也要累加
def kthSmallest2(matrix, k):
    if not matrix:
        return None
    if not matrix[0]:
        return None
    m, n = len(matrix), len(matrix[0])
    if k <= 0 or k > m*n:
        return None
    low, high = matrix[0][0], matrix[m-1][n-1]
    while low <= high:
        mid = (low+high)//2
        if countMatrixLeassEqual(matrix, mid) < k:
            low  = mid + 1
        else:
            high = mid - 1
    return low

if __name__ == "__main__":
    matrix = [[1,5],[10,11],[12,13]]
    for row in matrix:
        print(row)
    for k in range(1,len(matrix)*len(matrix[0])+1):
        print(k, kthSmallest(matrix, k))
    for k in range(1,len(matrix)*len(matrix[0])+1):
        print(k, kthSmallest2(matrix, k))

