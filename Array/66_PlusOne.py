# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode66: Plus One问题

def plusOne(digits):
    res = 0
    for item in digits:
        res = res*10 + item
    return [int(item) for item in str(res+1)]

if __name__ == "__main__":
    digits = [0]
    print(digits)
    print(plusOne(digits))
