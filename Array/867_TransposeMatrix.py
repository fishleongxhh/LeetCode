# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode867. Transpose Matrix问题

#A的行和列至少为1
def transpose(A):
    nrow, ncol = len(A), len(A[0])
    return [[A[i][j] for i in range(nrow)] for j in range(ncol)]

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    for row in A:
        print(row)
    print('\n')
    res = transpose(A)
    for row in res:
        print(row)
