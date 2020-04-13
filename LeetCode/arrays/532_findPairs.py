#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 0:52
# @Author  : Leslee

class Solution():
    def findPairs(self,nums,k):
        if k<0:
            return 0
        saw , diff = set(), set()
        for num in nums:
            if num -k in saw:
                diff.add(num-k)
            if num + k in saw:
                diff.add(num)
            saw.add(num)
        return len(diff)




s = Solution()
print(s.findPairs([3, 1, 4, 1, 5],2))


