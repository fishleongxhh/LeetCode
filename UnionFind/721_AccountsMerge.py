# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode721. Accounts Merge问题

from collections import defaultdict
from DisjointSet import DisjointSet

#在LeetCode上的运行速度很慢，需要进行优化
def accountsMerge(accounts):
    #将name和emails切割开，并将emails转化成集合
    accounts = [[record[0],set(record[1:])] for record in accounts]
    n = len(accounts)
    #初始化不相交集
    ds = DisjointSet(range(n))
    #一旦emails列表有重合，就进行union
    for i in range(n):
        for j in range(i):
            if accounts[i][1] & accounts[j][1]:
                ds.Union(i,j)
    #dic记录所有的不相交集
    dic = defaultdict(set)
    #逐个扫描，将同一个集合里的emails合并
    for i in range(n):
        loc = ds.Find(i)
        dic[loc] = dic[loc] | accounts[i][1]
    return [[accounts[loc][0]]+sorted(emails) for loc,emails in dic.items()]

if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    accounts += [['Mary','Mary@gmail.com'], ['John','johnjohn@gmail.com','johnnybravo@mail.com','john00@mail.com'], ['Mary','Mary@gmail.com','mary@mail.com']]
    accounts = [['Mary','Mary@gmail.com']]
    for row in accounts:
        print(row)
    print('\n')
    res = accountsMerge(accounts)
    for row in res:
        print(row)
