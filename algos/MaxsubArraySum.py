#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.15 10:50

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
class Solution:
    def maxSubArray(self,nums):
        oneSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            oneSum += nums[i]
            maxSum = max(maxSum,oneSum)
            if oneSum<0:
                oneSum = 0
        return maxSum
    # 动态规划
    def maxSubArray_Dongtai(self,nums):
        lenth = len(nums)
        for i in range(1,lenth):
            subMaxSum = max(nums[i]+nums[i-1],nums[i])
            nums[i] = subMaxSum
        return max(nums)


li =  [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
res = s.maxSubArray(li)
print(res)
# 针对这个问题，设sum[i]是第i个元素结尾的最大连续子数组的和，如果对于一个元素i，它前面的所有子区间的和都已经求得
# 那么就是sum[i]要么是现有区间最大值，要么是现有区间最大值+后面的一个元素。所以可以通过判断sum[i-1]+a[i]是否大于a[i]，
