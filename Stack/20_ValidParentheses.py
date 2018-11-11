# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode20: Valid Parentheses问题

def isValid(s):
    str_map = {')':'(', ']':'[', '}':'{'}
    stack = ['']
    for item in s:
        if (item in str_map) and (str_map[item] == stack[-1]):
            stack.pop()
        else:
            stack.append(item)
    if stack[-1]:
        return False
    return True

if __name__ == "__main__":
    s = '{}()'
    print(s)
    print(isValid(s))
