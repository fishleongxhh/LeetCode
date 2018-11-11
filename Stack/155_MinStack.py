# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode155: Min Stack问题


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if self.min_stack:
            self.min_stack.append(min(x, self.min_stack[-1]))
        else:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            self.data.pop()
            self.min_stack.pop()
        else:
            print('Error! Stack is Empty!')

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]
        else:
            print('Error! Stack is Empty!')
            return None        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print('Error! Stack is Empty!')
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    obj = MinStack()
    data = [5,2,4,6,7,2,8,9,4,6,9,0]
    print(data)
    for item in data:
        obj.push(item)
    for i in range(len(data)+3):
        print(obj.top())
        print(obj.getMin())
        obj.pop()
        print('\n')
