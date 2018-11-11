# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode125: Valid Palindrome问题

def isPalindrome(s):
    data_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    s = ''.join([item for item in s.lower() if item in data_set])
    return s == s[::-1]

if __name__ == "__main__":
    s = "race e car"
    print(s)
    print(isPalindrome(s))
