#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.24 10:18
import numpy as np
class Solution:
    def addOne(self,nums):
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=9:
                nums[i] = nums[i]+1
                return nums
            nums[i] = 0
        temp = [0]*(len(nums)+1)
        temp[0] = 1
        return temp
if __name__ == '__main__':
    s = Solution()

    print(s.addOne([8,9,9,9]))