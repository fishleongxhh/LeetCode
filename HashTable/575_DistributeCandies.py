# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode575: Distribute Candies问题

from collections import Counter

#candies的长度保证是偶数
def distributeCandies(candies):
    cnt = Counter(candies) #其实可以不用Counter类，直接用set，会更快
    return min(len(candies)//2, len(cnt.keys()))

if __name__ == "__main__":
    candies = [1,1,2,2,3,3,4,5,6,6]
    print(candies)
    print(distributeCandies(candies))
