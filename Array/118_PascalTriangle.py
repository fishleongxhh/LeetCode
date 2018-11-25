# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode118: Pascal's Triangle问题

#numRows非负
def generateRow(numRows):
    res = [1]
    if numRows%2:
        n1, n2 = (numRows+1)//2, 1
    else:
        n1, n2 = numRows//2, 0
    
    for i in range(1,n1):
        res.append(res[-1]*(numRows-i)//i)
    res.extend(res[::-1][n2:])
    return res

#生成全部行
def generate(numRows):
    res = []
    for n in range(numRows):
        res.append([1]*(n+1))
        for k in range(1,n):
            res[n][k] = res[n-1][k-1] + res[n-1][k]
    return res

if __name__ == "__main__":
    numRows = 0
    res = generate(numRows)
    for row in res:
        print(row)
