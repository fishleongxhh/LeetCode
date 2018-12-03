# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode200. Number of Islands问题

from DisjointSet import DisjointSet

def numIslands(grid):
    #获取行数和列数
    nrow = len(grid)
    if nrow == 0:
        return 0
    ncol = len(grid[0])
    if ncol == 0:
        return 0
    #所有1的坐标
    lands = set()
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] == "1":
                lands.add((i,j))
    #初始化不相交集
    ds = DisjointSet(list(lands))
    #扫描所有可能相邻的1，不断地union
    for point in lands:
        h_adj_point = (point[0], point[1]+1) #右邻居
        v_adj_point = (point[0]+1, point[1]) #下邻居
        #如果1的右邻居和下邻居都是1，则进行Union
        if h_adj_point in lands:
            ds.Union(point, h_adj_point)
        if v_adj_point in lands:
            ds.Union(point, v_adj_point)
    #最终返回不相交集的数目
    return ds.SetCnt

if __name__ == "__main__":
    grid = [[1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]]
    grid = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,1,0],
            [0,0,0,1,1]]
    grid = [[0],[1],[1],[0],[1],[0],[1]]
    #将grid里所有的元素变为字符串
    for i in range(len(grid)):
        grid[i] = [str(item) for item in grid[i]]
    for row in grid:
        print(row)
    print(numIslands(grid))

