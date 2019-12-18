#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.21 17:58
# 给定一个字符串 s，找到 s 中最长的回文子串。
class Solution(object):

    def maxChildpalindrome(self,s):
        sLen = len(s)
        i,j,max,c = 0,0,0,0
        for i in range(sLen):
            # 如果回文的长度是奇数
            for j in range(sLen-i):
                if i>=j:
                    if(s[i-j]!=s[i+j]):
                        break
                c = j  +1
            if c>max:
                max = c
            # 如果回文的长度是偶数
            for j in range(sLen-i-1):
                if i>=j:
                    if s[i-j] != s[i+j+1]:
                        break
                c = j  +2
            if c>max:
                max = c
        return max

if __name__ == '__main__':
    s = Solution()
    res = s.maxChildpalindrome("ddcacdd")
    print(res)
