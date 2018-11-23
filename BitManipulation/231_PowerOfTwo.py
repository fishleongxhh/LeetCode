# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode231: Power of Two问题

def isPowerOfTwo(n):
    return (n != 0) and ((n & (n-1)) == 0) #n和n-1按位取与可以消去n二进制表示中最右边的1，如果只有一个1，那么消除一次就会等于0

if __name__ == "__main__":
    for i in range(0,33):
        print(i, isPowerOfTwo(i))
