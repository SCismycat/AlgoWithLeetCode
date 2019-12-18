#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.24 9:56
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

class Solution(object):

    def maxSubArr(self,num):
        oneSum = 0
        maxSum = num[0]
        for i in range(len(num)):
            oneSum += num[i]
            if oneSum>maxSum:
                maxSum = oneSum

            if oneSum<0:
                oneSum = 0
        return maxSum



    def maxSubArray(self,num):
        if len(num)<=1:
            return num
        for i in range(1,len(num)):
            num[i] = num[i] + max(num[i-1],0)
        return max(num)

