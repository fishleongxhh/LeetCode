# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此程序用来求解LeetCode198--House Robber问题，此题等价于求解不连续子数组最大和问题，思想是动态规划

def house_robber(num):
    n = len(num)
    if n == 0:
        return 0
    if n == 1:
        return num[0]
    if n == 2:
        return max(num)
    A = [0]*n
    A[0], A[1] = num[0], max(num[0], num[1])
    for i in range(2,n):
        if A[i-2] == A[i-1]:
            A[i] = A[i-1] + num[i]
        else:
            A[i] = max(A[i-1], A[i-2]+num[i])
    return A[-1]

#事实上，你不需要存储所有的历史数据，只需要存储A[i-2]和A[i-1]就可以了
def house_robber2(num):
    n = len(num)
    if n == 0:
        return 0
    if n == 1:
        return num[0]
    if n == 2:
        return max(num)
    prev_prev, prev = num[0], max(num[0], num[1])
    for item in num[2:]:
        if prev_prev == prev:
            prev_prev, prev = prev, prev_prev+item
        else:
            prev_prev, prev = prev, max(prev, prev_prev+item)
    return prev

if __name__ == "__main__":
    num = [1,2,3,1]
    res = house_robber2(num)
    print(res)
