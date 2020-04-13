#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 0:39
# @Author  : Leslee
class Solution:
    def matrixReshape(self,nums,r,c):
        # 如果 行列相乘大于不等于需要shape的数量,返回
        if len(nums) * len(nums[0]) != r*c:
            return nums
        l = []
        new = []
        # 先来填充行
        for i in range(len(nums)):
            l += nums[i]
        #
        for j in range(0,len(l),c):
          new.append(l[j:j+c])
        return new


if __name__ == '__main__':
    s = Solution()
    nums =[[1,2],[3,4],[5,6],[7,8]]
    r = 2
    c = 4
    res = s.matrixReshape(nums,r,c)
    print(res)