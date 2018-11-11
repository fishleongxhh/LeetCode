#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def  miHomeGiftBag(p, M):
    row = len(p) + 1 
    col = M + 1 
    solutionMatrix = [[0 for c in range(col)] for r in range(row)]
    solutionMatrix[0][0] = 1 
    for i in range(1, col):
        solutionMatrix[0][i] = 0 
    for j in range(1, row):
        solutionMatrix[j][0] = 1 
        for k in range(1, col):
            solutionMatrix[j][k] = solutionMatrix[j - 1][k]
            if solutionMatrix[j][k] == 1:
                solutionMatrix[j][k] = solutionMatrix[j][k]
            elif (k - p[j - 1] >= 0) and (solutionMatrix[j][k - p[j - 1]] == 1): 
                solutionMatrix[j][k] = solutionMatrix[j][k - p[j - 1]] 
            else:
                solutionMatrix[j][k] = 0 
            if k == col - 1 and solutionMatrix[j][k] == 1:
                return 1
    return 0


#******************************结束写代码******************************

p_cnt = int(sys.stdin.readline().strip())
p = [int(item) for item in sys.stdin.readline().strip().split()]
M = int(sys.stdin.readline().strip())

print(miHomeGiftBag(p, M))

