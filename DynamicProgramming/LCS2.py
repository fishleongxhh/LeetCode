# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解两个字符串的最长公共子序列,子序列并不要求连续

def LCSCore(s1, s2):
    n1, n2 = len(s1), len(s2)
    tag = [[0]*n2 for i in range(n1)]
    direc = [['-']*n2 for i in range(n1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    tag[i][j] = 1
                else:
                    tag[i][j] = tag[i-1][j-1] + 1
                    direc[i][j] = '\\'
            else:
                if i == 0 and j == 0:
                    tag[i][j] = 0
                elif i == 0:
                    tag[i][j] = tag[i][j-1]
                    direc[i][j] = '-'
                elif j == 0:
                    tag[i][j] = tag[i-1][j]
                    direc[i][j] = '|'
                elif tag[i][j-1] > tag[i-1][j]:
                    tag[i][j] = tag[i][j-1]
                    direc[i][j] = '-'
                else:
                    tag[i][j] = tag[i-1][j]
                    direc[i][j] = '|'
    return tag, direc

def printLCS(s1, s2, tag, direc, nrow, ncol, res=[]):
    if nrow == 0 or ncol == 0:
        if tag[nrow][ncol] == 1:
            print(tag[nrow][ncol], (nrow,ncol))
            res.append(s2[ncol])
    else:
        if direc[nrow][ncol] == '\\':
            print(tag[nrow][ncol], (nrow,ncol))
            res.append(s2[ncol])
            printLCS(s1, s2, tag, direc, nrow-1, ncol-1, res)
        elif direc[nrow][ncol] == '|':
            printLCS(s1, s2, tag, direc, nrow-1, ncol, res)
        else:
            printLCS(s1, s2, tag, direc, nrow, ncol-1, res)

def LCS(s1, s2):
    if (not s1) or (not s2):
        return 0
    tag, direc = LCSCore(s1, s2)
    for item in tag:
        print(item)
    for item in direc:
        print(item)
    #接下来开始打印最长公共子序列
    res = []
    printLCS(s1, s2, tag, direc, len(s1)-1, len(s2)-1, res)
    print(''.join(res[::-1]))
    return tag[-1][-1]

if __name__ == "__main__":
    s1 = 'abcdfefji'
    s2 = 'abcdefhhhhjhi'
    print(s1, s2)
    print(LCS(s1, s2))
