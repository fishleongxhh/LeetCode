# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode342: Power of Four问题

def isPowerOfFour(num):
    if num <= 0:
        return False
    if (num & (num-1)) != 0: #首先它必须为2的幂
        return False
    cnt = 0
    while num != 1:
        num >>= 1
        cnt += 1
    return cnt%2 == 0 #其次，其二进制表示最右侧的1的右侧的0的数目为偶数

def isPowerOfFour2(num):
    if num <= 0:
        return False
    return (num & (num-1)) == 0 and (num - 1)%3 == 0  #一个正整数为4的幂当且仅当它为2的幂且减1之后能被4整除（4的幂减1之后均能被3整除，可以用二项式展开来证明）

if __name__ == "__main__":
    for i in range(0,1000):
        if isPowerOfFour2(i):
            print(i)
