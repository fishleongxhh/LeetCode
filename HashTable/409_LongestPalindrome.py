# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode409: Longest Palindrome问题

def longestPalindrome(s):
    dic = {}
    for item in s:
        dic[item] = dic.get(item, 0) + 1
    cnt = 0
    flag = False
    for item in dic:
        cnt += (dic[item] - dic[item]%2)
        flag = (flag or dic[item]%2)
    return cnt + int(flag)

if __name__ == "__main__":
    s = 'luoziye'
    print(s)
    print(longestPalindrome(s))
