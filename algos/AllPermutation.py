#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.22 17:26

class Solution(object):
    def allPermute(self,s):
        if len(s)<=1:
            return [s]
        allP = []
        # 固定第一个字符
        for i in range(len(s)):
            for j in self.allPermute(s[0:i]+s[i+1:]):
                allP.append(s[i]+j)
        return allP


if __name__ == '__main__':
    s = Solution()
    perm = s.allPermute("abc")
    print(set(perm))