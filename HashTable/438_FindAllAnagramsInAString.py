# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode438: Find All Anagrams in a String问题

from collections import Counter

def validAnagram(s,t):
    dic1, dic2 = {}, {}
    if len(s) != len(t):
        return False
    for item1, item2 in zip(s,t):
        dic1[item1] = dic1.get(item1,0) + 1
        dic2[item2] = dic2.get(item2,0) + 1
    return (dic1 == dic2)

def findAnagrams(s,p):
    n1, n2 = len(s), len(p)
    #if n1 < n2:
    #    return []
    res = map(lambda i: validAnagram(s[i:i+n2], p),range(0,n1-n2+1))
    return [loc for loc, item in enumerate(res) if item]

#解法2只需扫描一遍，计算一遍，比上面的解法效率高很多！
def findAnagrams2(s, p):
    len_s, len_p = len(s), len(p)
    cnt_s, cnt_p = Counter(s[:len(p)-1]), Counter(p)
    res = []
    for loc, item in enumerate(s[len_p-1:]):
        cnt_s[item] += 1
        start_index = loc
        if cnt_s == cnt_p:
            res.append(start_index)
        cnt_s[s[start_index]] -= 1
        if cnt_s[s[start_index]] == 0:
            del cnt_s[s[start_index]]
    return res


if __name__ == "__main__":
    s = 'a'*10000
    p = 'a'*100
    print(s,p)
    print(findAnagrams2(s,p))
