# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode290: Word Pattern问题

def wordPattern(pattern, str):
    words = str.split(' ')
    if len(pattern) != len(words):
        return False
    dic = {}
    for pat, item in zip(pattern, words):
        if pat in dic:
            if dic[pat] != item:
                return False
        else:
            if item in dic.values():
                return False
            else:
                dic[pat] = item
    return True

if __name__ == "__main__":
    pattern = 'abba'
    string = 'dog cat cat dog'
    print(pattern)
    print(string)
    print(wordPattern(pattern, string))
