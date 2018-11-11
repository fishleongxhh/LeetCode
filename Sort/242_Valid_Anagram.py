# -*- coding: utf-8 -*-
# Author:Xu Hanhui
# 此程序用来求解LeetCode242: Valid Anagram问题

#使用排序求解
def isAnagram(s,t):
    n1, n2 = len(s), len(t)
    if n1 != n2:
        return False
    s, t = sorted(s), sorted(t)
    for i in range(n1):
        if s[i] != t[i]:
            return False
    return True

#使用字典求解,这种解法比上述的排序要快
def isAnagram2(s,t):
    my_dict = {}
    for item in s:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    for item in t:
        if item not in my_dict:
            return False
        my_dict[item] -= 1
        if my_dict[item] == 0:
            del my_dict[item]
    if my_dict:
        return False
    return True
#采用字典的更简洁的方法
def isAnagram3(s,t):
    d1, d2 = {}, {}
    for item in s:
        d1[item] = d1.get(item, 0) + 1
    for item in t:
        d2[item] = d2.get(item, 0) + 1
    return d1 == d2

if __name__ == "__main__":
    s = 'hello'
    t = 'llohe'
    print(s)
    print(t)
    print(isAnagram(s,t))
    print(isAnagram2(s,t))
    print(isAnagram3(s,t))
