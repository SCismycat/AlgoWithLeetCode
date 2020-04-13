#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 0:36
# @Author  : Leslee


class Solution():
    def findMaxConsecutiveOnes(self,nums):
        res = 0
        tmp = 0
        for num in nums:
            if nums == 1:
                tmp += 1
                res = max(res,tmp)
            else:
                tmp = 0
        return res


    def findMaxConsecutiveOnes1(self,nums):
        sequence = "".join([str(x) for x in nums])
        newSeq = sequence.split("0")
        a = 0
        for seq in newSeq:
            a = max(a,len(seq))
        return a

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes1([1,1,0,1,1,1]))