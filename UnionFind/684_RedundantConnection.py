# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode684. Redundant Connection问题

from DisjointSet import DisjointSet

def findRedundantConnection(edges):
    n = len(edges) #点的数目
    ds = DisjointSet(range(1,n+1)) #初始化不相交集，下标从1开始
    PrevSetCnt = ds.SetCnt #上一步的不相交集数目
    for edge in edges:
        ds.Union(edge[0], edge[1])
        if PrevSetCnt == ds.SetCnt: #当加入一条边时不相交集的数目没有发生改变，则说明该边是多余的，形成了一个环
            return edge
        PrevSetCnt = ds.SetCnt

if __name__ == "__main__":
    edges = [[1,2], [3,4], [1,5], [4,5], [1,4]]
    print(edges)
    print('\n')
    print(findRedundantConnection(edges))
