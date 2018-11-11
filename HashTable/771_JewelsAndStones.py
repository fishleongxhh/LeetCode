# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode771: Jewels and Stones问题

def numJewelsInStones(J,S):
    jewels, cnt = set(J), 0
    for item in S:
        if item in jewels:
            cnt += 1
    return cnt

if __name__ == "__main__":
    J = ''
    S = ''
    print(J, S)
    print(numJewelsInStones(J,S))
