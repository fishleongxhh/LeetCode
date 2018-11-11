# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode447: Number of Boomerangs问题

def numberOfBoomerangs(points):
    n = len(points)
    dic = {i:{} for i in range(n)}
    for i in range(n):
        for j in range(i):
            dist = sum([(x-y)**2 for x,y in zip(points[i],points[j])])
            dic[i][dist] = dic[i].get(dist,0) + 1
            dic[j][dist] = dic[j].get(dist,0) + 1
    return sum([sum([d*(d-1) for d in dic[i].values()]) for i in dic])

if __name__ == "__main__":
    points = [[1,1],[0,0],[1,0],[0,1]]
    for point in points:
        print(point)
    print(numberOfBoomerangs(points))
