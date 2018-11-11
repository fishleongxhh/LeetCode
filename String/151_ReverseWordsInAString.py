# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode151: Reverse Words in a String问题

def reverseWords(s):
    res = s.split() #会根据空格进行分割，字符串首尾的空格会被忽略，中间多个空格会被视为一个空格处理
    res.reverse()
    return ' '.join(res)

if __name__ == "__main__":
    s = "   the  sky     is blue.  "
    print(s)
    print(reverseWords(s))
