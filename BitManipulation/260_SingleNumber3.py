# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode260: Single Number3问题

#找到pivot中从右往左第一个1出现的位置
#pivot的二进制表示中至少有一个1
def findBit1(pivot):
    ind = 0
    while not (pivot & 1):
        ind, pivot = ind+1, pivot>>1
    return ind

#判断一个数的二进制表示，从右往左第ind+1位是否为1
def isBit1(item, ind):
    return (item >> ind) & 1

def singleNumber(nums):
    if len(nums) < 2:
        return None
    pivot = 0
    for item in nums:
        pivot = pivot ^ item
    indBit1 = findBit1(pivot)
    res1 = res2 = 0
    for item in nums:
        if isBit1(item, indBit1):
            res1 = res1 ^ item
        else:
            res2 = res2 ^ item
    return [res1, res2]

if __name__ == "__main__":
    nums = [1,2,1,3,2,4,3,5,5,7]
    print(sorted(nums))
    print(singleNumber(nums))
