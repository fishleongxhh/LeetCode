# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode455: Assign Cookies问题

def findContentChildren(g, s):
    g.sort()
    s.sort()
    i, j, max_cnt = 0, 0, 0
    len1, len2 = len(g), len(s)
    while i < len1 and j < len2:
        if s[j] < g[i]:
            j += 1
        else:
            i, j, max_cnt = i+1, j+1, max_cnt+1
    return max_cnt

if __name__ == "__main__":
    g = [1,4,42,5,6,6,7]
    s = [1,65,6,7,8,8,2]
    print(g, s)
    print(findContentChildren(g, s))
    print(g, s)
