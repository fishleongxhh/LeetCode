# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode11. Container With Most Water问题

#height的长度至少为2,即至少有两根柱子
def maxArea(height):
    MaxArea = CurrArea = 0
    start, end = 0, len(height)-1
    while start < end:
        #较短的柱子向着另一端移动,因为短柱子固定住之后，另一端无论如何移动，所夹的面积都不会超过start和end之间的面积
        if height[start] < height[end]:
            CurrArea = height[start]*(end-start)
            start += 1
        else:
            CurrArea = height[end]*(end-start)
            end -= 1
        if CurrArea > MaxArea:
            MaxArea = CurrArea
    return MaxArea

if __name__ == "__main__":
    height = [1,8,6]
    print(height)
    print(maxArea(height))
