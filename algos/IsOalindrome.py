#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.21 14:35

class Solution(object):
    def isPalindrome(self,s):
        if len(s)==0:
            return
        start,end = 0,len(s)-1
        while(start<end):
            for i in range(len(s)):
                if(s[start]!=s[end]):
                    return False
                start+=1
                end -=1
        return True



if __name__ == '__main__':
    s = Solution()
    name = s.isPalindrome("ddccccdd")
    print(name)