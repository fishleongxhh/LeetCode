# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode830. Positions of Large Groups问题

#S包含的全是小写字母
#由于存在频繁的赋值操作，所以时间上较慢，可以继续优化
def largeGroupPositions(S):
    res = []
    prev, start, cnt = '', -1, 0 #初始化
    for loc, item in enumerate('{}_'.format(S)): #为了能对最后一个字母做正确的统计，最后添加一个不会出现的字符_
        if item == prev:
            cnt += 1
        else:
            if cnt >= 3:
                res.append([start,loc-1]) #收集Large Group
            prev, cnt, start = item, 1, loc #更新
    return res

if __name__ == "__main__":
    S = ''
    print(S)
    res = largeGroupPositions(S)
    for record in res:
        print(record)
