# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此程序用来求解LeetCode70：爬楼梯问题，需要用到动态规划，递推公式（其实就是斐波那契数列）

#参数n是一个正数
def ClimbingStairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    prev, curr = 1, 2
    for i in range(3,n+1):
        prev, curr = curr, prev+curr
    return curr

if __name__ == "__main__":
    for i in range(1,11):
        print(ClimbingStairs(i))
