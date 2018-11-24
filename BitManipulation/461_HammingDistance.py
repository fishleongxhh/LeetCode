# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode461: Hamming Distance问题

#计算两个非负整数的hamming距离
def hammingDistance(x, y):
    xor = x^y #按位取异或
    cnt = 0
    while xor:
        xor = (xor & (xor-1)) #消去最右侧的1
        cnt += 1 #计算1bit的数目
    return cnt

if __name__ == "__main__":
    x, y = 10, 1
    print(x, y)
    print(bin(x), bin(y))
    print(hammingDistance(x, y))
