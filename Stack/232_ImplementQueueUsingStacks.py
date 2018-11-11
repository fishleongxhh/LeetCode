# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode232: Implement Queue using Stacks问题

class MyQueue:
    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, x):
        self.data.append(x)
        self.size += 1

    def empty(self):
        #return len(self.data) == self.start_index
        return self.size == 0

    def pop(self):
        if not self.empty():
            item = self.data[0]
            self.data = self.data[1:]
            self.size -= 1
            return item
        else:
            print("Queue is Empty!")
            return None

    def peek(self):
        if not self.empty():
            return self.data[0]
        else:
            print("Queue is Empty")
            return None

if __name__ == "__main__":
    data = [1,3,4,5,6,2,7,8,9,0]
    print(data)
    obj = MyQueue()
    for item in data:
        obj.push(item)
        print(obj.data)
    for i in range(len(data)+3):
        obj.pop()
        print(obj.data)
