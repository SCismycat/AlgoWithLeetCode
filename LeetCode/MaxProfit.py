#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.11 14:03

def maxProfit(prices):
    if len(prices) <=1:
        return 0
    max_profit = 0
    min_pirce = prices[0]

    for i in range(len(prices)):
        max_profit = max(max_profit,prices[i] - min_pirce)
        min_pirce = min(min_pirce,prices[i])
    return max_profit
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 只要后一天比前一天大，就卖出
def maxProfit2(prices):
    if len(prices) <=1:
        return 0
    max_profit = 0
    for i in range(1,len(prices)):
        differ = prices[i] - prices[i-1]
        if differ>0:
            max_profit += differ
    return max_profit
if __name__ == '__main__':
    print(maxProfit2([7,1,5,3,6,4]))