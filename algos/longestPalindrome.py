#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.21 11:33

class Solution(object):
    def longestPalindrome(self,string):
        hs = set()
        count = 0
        if(len(string)==0):
            return 0
        for i in range(len(string)):
            if string[i] in hs:
                hs.remove(string[i])
                count +=1
            else:
                hs.add(string[i])
        if len(hs)==0:
            return count*2
        else:
            return count*2+1

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abccccdd"))