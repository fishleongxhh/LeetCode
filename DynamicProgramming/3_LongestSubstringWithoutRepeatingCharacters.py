# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode3: Longest Substring Without Repeating Characters问题

def lengthOfLongestSubstring(s):
    res, dic = [0]*len(s), {} #res用来记录动态规划计算过程中的结果，dic用来记录一个字符上次出现的位置
    maxLen = 0 #用来记录最大长度
    for i, item in enumerate(s):
        if item not in dic:
            res[i] = res[i-1]+1 if i>0 else 1
        else:
            gap = i - dic[item]
            res[i] = gap if gap <= res[i-1] else res[i-1]+1
        dic[item] = i
        maxLen = maxLen if res[i] <= maxLen else res[i]
    return maxLen

if __name__ == "__main__":
    s = 'aaaaaaa'
    print(s)
    print(lengthOfLongestSubstring(s))
