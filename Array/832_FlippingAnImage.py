# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode832. Flipping an Image问题

#A矩阵的长和宽至少是1
def flipAndInvertImage(A):
    nrow, ncol = len(A), len(A[0])
    for i in range(nrow):
        #A[i] = [1-item for item in A[i][::-1]] #以下一段可以简化成这一句
        start, end = 0, ncol-1
        while start <= end:
            A[i][start], A[i][end] = 1-A[i][end], 1-A[i][start]
            start += 1
            end -= 1
    return A

if __name__ == "__main__":
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    for row in A:
        print(row)
    res = flipAndInvertImage(A)
    print('\n')
    for row in res:
        print(row)
