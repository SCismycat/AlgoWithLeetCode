#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.24 9:41

class Solution(object):
    def twoSum(self,data,sum):
        # 排序
        data = sorted(data)
        start, end = 0,len(data)-1
        while(start<end):
            if data[start] == sum-data[end]:
                return (data[start],data[end])
            elif data[start]>sum-data[end]:
                end -= 1
            elif data[start]<sum-data[end]:
                start += 1

if __name__ == '__main__':
    data = [1, 2,4,7,11,15]
    s = Solution()
    print(s.twoSum(data,15))