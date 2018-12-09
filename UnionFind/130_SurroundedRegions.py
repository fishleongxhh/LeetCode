# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode130. Surrounded Regions问题

from DisjointSet import DisjointSet

def solve(board):
    if board: #如果board为空则不做任何处理
        nrow, ncol = len(board), len(board[0])
        inner, border = [], [] #记录所有"O"出现的位置，分为内部和边界处
        #扫描,记录所有"O'的位置
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == "O":
                    if i==0 or i==nrow-1 or j==0 or j==ncol-1:
                        border.append((i,j))
                    else:
                        inner.append((i,j))
        #如果边界上无O,则全部转换
        if not border:
            for loc in inner:
                board[loc[0]][loc[1]] = "X"
        else:
            #初始化不相交集
            ds = DisjointSet(border+inner)
            #将边界上的"O"点Union起来
            pivot = border[0]
            for loc in border[1:]:
                ds.Union(pivot, loc)
            #遍历inner和border,建立必要的连接
            for loc in border+inner:
                if loc[0] < nrow-1:
                    if board[loc[0]+1][loc[1]] == "O":
                        ds.Union(loc, (loc[0]+1,loc[1]))
                if loc[1] < ncol-1:
                    if board[loc[0]][loc[1]+1] == "O":
                        ds.Union(loc, (loc[0],loc[1]+1))
            #遍历inner中的点，若其不与border中的点同类，则转换
            for loc in inner:
                if ds.Find(loc) != ds.Find(pivot):
                    board[loc[0]][loc[1]] = "X"

if __name__ == "__main__":
    board = [["O","X","X","X"],["X","O","O","X"],["O","O","O","X"],["X","O","X","O"]]
    board = []
    for row in board:
        print(row)
    print("\n")
    solve(board)
    for row in board:
        print(row)
