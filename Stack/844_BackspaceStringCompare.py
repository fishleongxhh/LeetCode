# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode844: Backspace String Compare问题

def backspaceCompare(S, T):
    stack1, stack2 = [], []
    for item in S:
        if item != '#':
            stack1.append(item)
        if item == '#' and len(stack1) > 0:
            stack1.pop()
    for item in T:
        if item != '#':
            stack2.append(item)
        if item == '#' and len(stack2) > 0:
            stack2.pop()
    return stack1 == stack2

if __name__ == "__main__":
    S = '###a#c######'
    T = '########b#####'
    print(S, T)
    print(backspaceCompare(S, T))
