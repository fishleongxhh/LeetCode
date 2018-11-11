# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode389: Find the Difference问题

def findTheDifference(s, t):
    dic = {}
    for item in s:
        dic[item] = dic.get(item, 0) + 1
    for item in t:
        dic[item] = dic.get(item, 0) - 1
        if dic[item] == -1:
            return item

if __name__ == "__main__":
    s = ''
    t = 'h'
    print(s,t)
    print(findTheDifference(s,t))
