# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode345: Reverse Vowels of a String问题

vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

def reverseVowels(s):
    n = len(s)
    s = list(s)
    start, end = 0, n-1
    while start < end:
        while start < end and s[start] not in vowels:
            start += 1
        while start < end and s[end] not in vowels:
            end -= 1
        if start >= end:
            return ''.join(s)
        else:
            s[start], s[end] = s[end], s[start]
        start, end = start+1, end-1
    return ''.join(s)

if __name__ == "__main__":
    s = "leetcode"
    print(s)
    print(reverseVowels(s))
