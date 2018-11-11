# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode387: First Unique Character in a String问题

def firstUniqChar(s):
    dic = {}
    uniq_str = set()
    for loc, item in enumerate(s):
        if item in dic:
            uniq_str.discard(item)
        else:
            dic[item] = loc
            uniq_str.add(item)
    res = [dic[item] for item in uniq_str]
    if res:
        return min(res)
    return -1

if __name__ == "__main__":
    s = 'huhuihui'
    print(s)
    print(firstUniqChar(s))
