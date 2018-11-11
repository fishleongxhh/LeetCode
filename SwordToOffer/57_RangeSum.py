# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解剑指offer57题第二小题: 和为s的连续正数序列

def RangeSum(s):
    start, end, currSum = 1, 2, 3
    while start <= s//2:
        if currSum == s:
            print(list(range(start, end+1)))
            end += 1
            currSum += end
        elif currSum < s:
            end += 1
            currSum += end
        else:
            currSum -= start
            start += 1

if __name__ == "__main__":
    for s in range(30):
        print(s)
        RangeSum(s)
        print('\n')
