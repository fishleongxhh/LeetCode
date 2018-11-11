# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode463: Island Perimeter问题


def sumAdj(i, j, nrow, ncol, grid):
    cnt = 0
    if j > 0:
        cnt += grid[i][j-1]
    if j < (ncol-1):
        cnt += grid[i][j+1]
    if i > 0:
        cnt += grid[i-1][j]
    if i < (nrow-1):
        cnt += grid[i+1][j]
    return cnt

def islandPerimeter(grid):
    cnt_of_one, cnt_of_adj = 0, 0
    nrow, ncol = len(grid), len(grid[0])
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] == 1:
                cnt_of_one += 1
                cnt_of_adj += sumAdj(i,j,nrow,ncol,grid)
    return 4*cnt_of_one - cnt_of_adj


if __name__ == "__main__":
    grid = [[0,1,0,0],
            [1,1,1,1],
            [0,1,0,0],
            [1,1,0,0]]
    print(grid)
    print(islandPerimeter(grid))
