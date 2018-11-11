# -*- coding: utf-8 -*-

import sys

M = int(sys.stdin.readline().strip())
data = []
for i in range(M):
    data.append([int(item) for item in sys.stdin.readline().strip().split(" ")])
print(data)
edges = []
npoints = 0
index_map = {}
for i in range(M):
    for j in range(M):
        if data[i][j] == 1:
            index_map[(i,j)] = npoints
            npoints += 1
            if i-1 >= 0:
                if data[i-1][j] == 1:
                    edges.append([index_map[(i-1,j)], index_map[(i,j)]])
            if j-1 >= 0:
                if data[i][j-1] == 1:
                    edges.append([index_map[(i,j-1)], index_map[(i,j)]])
print(edges)
print(npoints)

class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))
        self.count = n
 
    def find_set(self, x):
       if self.set[x] != x:
           self.set[x] = self.find_set(self.set[x])  # path compression.
       return self.set[x]
 
    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1
 
 
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        union_find = UnionFind(n)
        for i, j in edges:
            union_find.union_set(i, j)
        return union_find.count

res = Solution()
print(res.countComponents(npoints, edges))
