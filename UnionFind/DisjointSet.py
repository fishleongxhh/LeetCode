# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来实现不相交集的类定义及有关的方法

class DisjointSet:
    #根据nums里的元素初始化一个不相交集
    def __init__(self, nums):
        self.size = len(nums)
        self.__HashMap = dict(zip(nums, range(self.size)))
        self.__DisjSet = [-1]*self.size

    #使用了路径压缩的Find操作
    def __FindCore(self, loc):
        if self.__DisjSet[loc] < 0:
            return loc
        else:
            self.__DisjSet[loc] = self.__FindCore(self.__DisjSet[loc])
            return self.__DisjSet[loc]

    def Find(self, item):
        loc = self.__HashMap[item]
        return self.__FindCore(loc)

    #基于高度的Union操作
    def __UnionCore(self, root1, root2):
        if self.__DisjSet[root1] < self.__DisjSet[root2]: #root1更深
            self.__DisjSet[root2] = root1
        else:
            if self.__DisjSet[root1] == self.__DisjSet[root2]:
                self.__DisjSet[root2] -= 1
            self.__DisjSet[root1] = root2

    def Union(self, item1, item2):
        #首先查到两个元素的root
        root1 = self.Find(item1)
        root2 = self.Find(item2)
        #执行Union操作
        if root1 != root2:
            self.__UnionCore(root1, root2)

if __name__ == "__main__":
    nums = ['a','s','d','q','w','e','z','x','c']
    print(nums)
    DS = DisjointSet(nums)
    print(DS.size)
    print(DS.Find('a')==DS.Find('q'))
