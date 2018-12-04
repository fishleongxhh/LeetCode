# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode3: Longest Substring Without Repeating Characters问题

def lengthOfLongestSubstring(s):
    #res[i]记录以s[i]结尾同时不包含重复字符的最长连续子数组的长度
    #dic用来记录一个字符上次出现的位置
    res, dic = [0]*len(s), {}
    maxLen = 0 #用来记录最大长度
    for i, item in enumerate(s):
        if item not in dic:
            res[i] = res[i-1]+1 if i>0 else 1
        else:
            gap = i - dic[item]
            res[i] = gap if gap <= res[i-1] else res[i-1]+1 #这句话逻辑没有问题，因为s[i-1]之前res[i-1]长度的字符串都没有重复字符
        dic[item] = i
        maxLen = maxLen if res[i] <= maxLen else res[i]
    return maxLen

if __name__ == "__main__":
    s = 'aaaaaaa'
    print(s)
    print(lengthOfLongestSubstring(s))
