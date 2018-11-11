# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode557: Reverse Words in a String2问题

def reverseWords(s):
    res = map(lambda x:x[::-1], s.split())
    return ' '.join(res)

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(s)
    print(reverseWords(s))
