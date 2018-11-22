# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode5: Longest Palindromic Substring问题

#此解法有误！
#此程序用来求解两个字符串的最长公共字串
def LCS(s1, s2):
    m, n = len(s1), len(s2)
    if (not m) or (not n):
        return ''
    flag = [0]*n
    maxLen, end = 0, -1
    for i in range(m):
        for j in range(n-1, -1, -1): #从后往前更新tag数组
            if s1[i] == s2[j]:
                flag[j] = 1 if i == 0 or j == 0 else flag[j-1] + 1
            else:
                flag[j] = 0
            if flag[j] > maxLen:
                maxLen, end = flag[j], j
    return s2[(end+1-maxLen):(end+1)]

def longestPalindrome(s):
    return LCS(s, s[::-1])

if __name__ == "__main__":
    s = "avhfuafhabbbbbba"
    print(s)
    print(longestPalindrome(s))
