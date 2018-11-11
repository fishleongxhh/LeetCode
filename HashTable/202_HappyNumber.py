# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode202: Happy Number问题，需要用到Hash Table

def getSquare(n):
    res = 0
    while n != 0:
        res = res + (n%10)**2
        n = n//10
    return res

def isHappy(n):
    my_set = {n}
    while True:
        n = getSquare(n)
        if n == 1:
            return True
        if n in my_set:
            return False
        my_set.add(n)

if __name__ == "__main__":
    n = 100
    print(n)
    print(isHappy(n))
