# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode122: Best Time to Buy and Sell Stock2问题

def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    max_profit, prev_item = 0, prices[0]
    for curr_item in prices[1:]:
        max_profit += max(0, curr_item - prev_item)
        prev_item = curr_item
    return max_profit

if __name__ == "__main__":
    prices = [7,6,4,3,1]
    print(prices)
    print(maxProfit(prices))
