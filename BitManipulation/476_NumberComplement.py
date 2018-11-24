# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode476: Number Complement问题

def findComplement(num):
    n = len(bin(num))-2 #获取其二进制表示的位数
    return num ^ (2**n-1)

if __name__ == "__main__":
    num = 1
    print(num, findComplement(num))
