# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode119: Pascal's Triangle2问题

#rowIndex从0开始
def getRow(rowIndex):
    res, numRows = [1], rowIndex+1
    if numRows%2:
        n1, n2 = (numRows+1)//2, 1
    else:
        n1, n2 = numRows//2, 0
    
    for i in range(1,n1):
        res.append(res[-1]*(numRows-i)//i)
    res.extend(res[::-1][n2:])
    return res

if __name__ == "__main__":
    n = 10
    for i in range(n):
        print(getRow(i))
