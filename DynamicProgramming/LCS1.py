# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解两个字符串的最长公共子串(及其长度)

def LCSCore(s1, s2):
    n1, n2 = len(s1), len(s2)
    end, maxLen = 0, 0
    tag = [0]*n2
    for i in range(n1):
        for j in range(n2-1,-1,-1):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    tag[j] = 1
                else:
                    tag[j] = tag[j-1] + 1
            else:
                tag[j] = 0  #这一步很重要！！不能省略！！
            if tag[j] > maxLen:
                end, maxLen = j, tag[j]
    return s2[end+1-maxLen:end+1]

#此程序用来求解两个字符串的最长公共字串和其长度
def LCS(s1, s2):
    lcs = LCSCore(s1,s2)
    return [lcs, len(lcs)]

#还可以不要求连续，求两个字符串的最长公共子序列及其长度

if __name__ == "__main__":
    s1 = '12345'
    s2 = '1232345'
    print(s1, s2)
    print(LCS(s1, s2))
