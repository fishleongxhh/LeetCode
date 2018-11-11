# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来实现能够常数时间求解最大值的队列

class QueueElement:
    def __init__(self, x, ind):
        self.item, self.index = x, ind

class QueueMax:
    def __init__(self):
        self.data, self.__maxData = [], []
        self.size, self.currIndex = 0, 0

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            print("The Queue is Empty!")
            return None
        else:
            return self.data[0].item

    def getMax(self):
        if self.isEmpty():
            print("The Queue is Empty!")
            return None
        return self.__maxData[0].item

    def push(self, x):
        currElement = QueueElement(x, self.currIndex)
        self.data.append(currElement)
        self.size, self.currIndex = self.size+1, self.currIndex+1
        while self.__maxData and self.__maxData[-1].item <= x:
            self.__maxData.pop()
        self.__maxData.append(currElement)

    def pop(self):
        if self.isEmpty():
            print("The Queue is Empty!")
            return None
        popElement = self.data.pop(0)
        self.size -= 1
        if self.__maxData[0].index == popElement.index:
            self.__maxData.pop(0)

if __name__ == "__main__":
    nums = [5,1,3,2,4,7,8,6,9]
    q = QueueMax()
    for item in nums:
        q.push(item)
        print(q.size, q.getMax())



