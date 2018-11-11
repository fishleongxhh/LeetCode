# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode240: Search a 2D Matrix2问题

def searchMatrix(matrix, target):
    nrow = len(matrix)
    if not nrow:
        return False
    ncol = len(matrix[0])
    if not ncol:
        return False
    i, j = 0, ncol-1
    while i < nrow and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False

if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]]
    matrix = [[],[],[]]
    for row in matrix:
        print(row)
    print("\n")
    for target in [5,7,13,16,17,20,22,25]:
        print(target, searchMatrix(matrix, target))
