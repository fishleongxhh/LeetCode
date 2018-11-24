# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode693: Binary Number with Alternating Bits问题

#输入为正数
def hasAlternatingBits(n):
    x = (n<<1) if (n&1) else (n<<1)+1 #将n左移1位,如果n为偶数,则要加1
    flag = (x^n)
    return flag == (1<<(len(bin(flag))-2))-1 #flag每一位都是1，其值为2**i-1
    #print(n, bin(n)[2:], bin(x)[2:], bin(flag)[2:])

if __name__ == "__main__":
    for n in range(1,200):
        if hasAlternatingBits(n):
            print(n, bin(n))
