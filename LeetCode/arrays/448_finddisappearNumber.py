#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 0:35
# @Author  : Leslee
class Solution:
    def findDisappearNumbers(self,nums):
        output = []
        nums = sorted(nums)
        nums = list(set(nums))
        for idx,num in enumerate(nums):
            if idx+1 != num:
                output.append(idx+1)
        return output

    def findDisappearNumbers_1(self,nums):
        output = []
        hash_table = {}
        for num in nums:
            hash_table[num] = 0
        for num in range(1,len(nums)+1):
            if num not in hash_table:
                output.append(num)
        return output
    # 牛逼做法来了！把每个元素看成下标。在原数组中把元素的下标对应的元素置为负的，然后
    # 没变负的就是没出现的元素，下标是自然有序的。所以，为正的所在的位置就是缺失的元素
    def findDisappearNumbers_2(self,nums):
        output = []
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        for idx,num in enumerate(nums):
            if num>0:
                output.append(idx+1)
        return output

a = [4,3,2,7,8,2,3,1]
s = Solution()
print(s.findDisappearNumbers_2(a))