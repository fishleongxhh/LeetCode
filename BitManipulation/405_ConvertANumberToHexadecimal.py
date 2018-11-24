# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode405: Convert a Number to Hexadecimal问题

def toHexPositive(num):
    dic = dict(zip(range(0,16), "0123456789abcdef"))
    res = []
    while num:
        res.append(dic[num%16])
        num //= 16
    return ''.join(res[::-1])

def toHex(num):
    if num > 0:
        return toHexPositive(num)
    elif num == 0:
        return 0
    else:
        return toHexPositive((1<<32)+num)

#''.join('0123456789abcdef'[(num >> 4 * i) & 15] for i in range(8))[::-1].lstrip('0') or '0'

if __name__ == "__main__":
    for num in range(-20,1):
        print(num, hex(num), toHex(num))
