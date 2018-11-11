# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode205: Isomorphic Strings问题，需要用到HashMap

#s和t应是等长的字符串
def isIsomorphic(s,t):
    n1, n2 = len(s), len(t)
    if n1 != n2:
        return False
    my_dict = {}
    for i in range(n1):
        if s[i] not in my_dict:
            if t[i] in my_dict.values():
                return False
            my_dict[s[i]] = t[i]
        if my_dict[s[i]] != t[i]:
            return False
    return True

if __name__ == "__main__":
    s, t = 'ab', 'aa'
    print(s,t)
    print(isIsomorphic(s,t))
