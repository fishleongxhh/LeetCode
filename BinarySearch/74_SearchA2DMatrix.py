# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode74: Search a 2D Matrix问题

def searchMatrix(matrix, target):
    nrow = len(matrix)
    if not nrow:
        return False
    ncol = len(matrix[0])
    if not ncol:
        return False
    start, end = 0, nrow*ncol-1
    while start <= end:
        mid = (start+end)//2
        i, j = (mid-mid%ncol)//ncol, mid%ncol
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    for row in matrix:
        print(row)
    print("\n")
    for target in range(10):
        print(target, searchMatrix(matrix, target))
