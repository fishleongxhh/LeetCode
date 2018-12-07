# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode547. Friend Circles问题

from DisjointSet import DisjointSet

def findCircleNum(M):
    n = len(M)
    if n == 0:
        return 0
    #初始化不相交集
    DS = DisjointSet(range(n))
    #扫描M矩阵，完成Union操作
    for i in range(n):
        for j in range(i):
            if M[i][j] == 1:
                DS.Union(i,j)
    #返回不相交集的数目
    return DS.SetCnt

if __name__ == "__main__":
    M = [[1,1,0], [1,1,0],[0,0,1]]
    print(findCircleNum(M))
