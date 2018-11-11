# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解剑指offer16：数组的整数次方

def pow(x,n):
    if x == 0 and n < 0:
        return None
    if n == 0:
        res = 1
    elif n > 0:
        if n%2:
            res = (pow(x,n//2)**2)*x
        else:
            res = pow(x,n//2)**2
    else:
        res = 1/pow(x,-n)
    return res

if __name__ == "__main__":
    x, n = 0, 4
    print(x,n,pow(x,n))
