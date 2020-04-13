#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 23:49
# @Author  : Leslee

# 当头棒喝：时间复杂度要求o(n)，所以sort(O(nlog(n)))不可以用
# 设置三个变量，分别记录三个数，一次for循环比较输出
class Solution:
    def thirdMax(self,nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) ==2:
            return max(nums[0],nums[1])

        max1 = -float('inf')
        max2 = -float('inf')
        max3 = -float('inf')

        f = True
        flag = 0
        for i in range(0,len(nums)):
            if nums[i] == -float('inf') and f:
                flag += 1
                f = False # 判断有没有无穷小，无穷小是必须被抛弃的

            if nums[i]>max1:
                flag +=1
                max3 = max2 # 第二大的给第三大的
                max2 = max1 # 最大的给第二大的
                max1 = nums[i] # 更新最大的
            elif nums[i]>max2 and nums[i]<max1:
                flag += 1
                max3 = max2 # 数在第一和第二中间，把第二挤到第三
                max2 = nums[i]
            elif nums[i]>max3 and nums[i] <max2:
                flag += 1
                max3 = nums[i]
        return max3 if flag>=3 else max1
nums = [12,3,4,5,3,5]
s = Solution()
print(s.thirdMax(nums))




