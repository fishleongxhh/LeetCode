# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode225: Implement Stack using Queues问题

class MyStack():
    def __init__(self):
        self.data = []
        self.size = 0
    
    def empty(self):
        return self.size == 0

    def push(self, x):
        self.data.append(x)
        self.size += 1

    def pop(self):
        if not self.empty():
            item = self.data[-1]
            self.size -= 1
            self.data = self.data[:self.size]
            return item
        else:
            print("The Stack is Empty!")
            return None

    def top(self):
        if not self.empty():
            return self.data[-1]
        else:
            print("The Stack is Empty!")
            return None

if __name__ == "__main__":
    data = [1,3,4,2,5]
    print(data)
    stack_instance = MyStack()
    for item in data:
        stack_instance.push(item)
        print(stack_instance.data)
    for i in range(6):
        print(stack_instance.pop())
