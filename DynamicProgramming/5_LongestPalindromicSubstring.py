# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode5: Longest Palindromic Substring问题

#Dynamic Programming
def longestPalindrome(s):
    n = len(s)
    MaxLen = start = end = 0
    tag = [False]*n #在第j个循环中，tag[i]记录s[i:j+1]子字符串是否是回文串
    for j in range(n): #列
        for i in range(j+1): #行
            if i == j:
                tag[i] = True
            elif i == (j-1):
                tag[i] = (s[i]==s[j])
            else:
                tag[i] = tag[i+1] and (s[i]==s[j])
            if tag[i] and (j-i+1) > MaxLen:
                MaxLen = (j-i+1)
                start, end = i, j+1
    return s[start:end]

#Expand Around Center
#从start和end往两边扩散，找到最长的回文串
def expandAroundCenter(s, start, end):
    while start >=0 and end < len(s) and s[start] == s[end]:
        start, end = start-1, end+1
    #注意，循环完成之后最长的回文串为s[start+1:end-1]
    return end-start-1

def longestPalindrome2(s):
    n = len(s)
    MaxLen = start = end = 0
    for i in range(n):
        len1 = expandAroundCenter(s, i, i)
        if i == n-1:
            len2 = 0
        else:
            len2 = expandAroundCenter(s, i, i+1)
        CurrLen = max(len1, len2)
        if CurrLen > MaxLen:
            MaxLen = CurrLen
            start, end = i-(MaxLen-1)//2, i+MaxLen//2
    return s[start:(end+1)]

if __name__ == "__main__":
    s = "vhashfjayuhfagfqyuhfbsjzbzbzhf"
    print(s)
    print(longestPalindrome(s))
    print(longestPalindrome2(s))
