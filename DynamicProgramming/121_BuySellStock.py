# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此程序用来求解LeetCode121: Best Time to Buy and Sell Stock，求解需要用到动态规划的思想

def MaxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    MaxGap = 0
    MinItem = prices[0]
    for item in prices[1:]:
        MaxGap = max(MaxGap, item-MinItem)
        MinItem = min(item, MinItem)
    return MaxGap

if __name__ == "__main__":
    prices = [0,1,5,3,2,4]
    print(MaxProfit(prices))
