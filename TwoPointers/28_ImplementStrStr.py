# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode28: Implement strStr问题

def strStr(haystack, needle):
    len1, len2 = len(haystack), len(needle)
    if len2 > len1:
        return -1
    if len2 == 0:
        return 0
    start = 0
    while start <= len1-len2:
        if haystack[start] != needle[0]:
            start += 1
        elif haystack[start:(start+len2)] == needle:
            return start
        else:
            start += 1
    return -1

if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    print(haystack, needle)
    print(strStr(haystack, needle))
