# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此程序用来求解LeetCode746: Min Cost Climbing Stairs, 求解需要用到动态规划的思想

#此题的解答思路来源于LeetCode746讨论区一位楼主的回答
#很多解答都是从后向前递进，但是该解答是从前向后递进，思路比较清晰
#根据他的思路写出的代码效率也很高
def MinCostClimbingStairs(cost):
    n = len(cost)
    if n <= 1:
        return 0
    if n == 2:
        return min(cost)
    #prev_cost记录如果上一脚踏在前一个阶梯时的最小损失，curr_cost记录上一脚踏在当前阶梯时的最小损失
    prev_cost, curr_cost = cost[0], cost[1]
    for i in range(2,n):
        prev_cost, curr_cost = curr_cost, cost[i]+min(prev_cost, curr_cost)
    return min(prev_cost, curr_cost)

if __name__ == "__main__":
    cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(MinCostClimbingStairs(cost))
