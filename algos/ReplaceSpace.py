#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.21 10:14
# 将一个字符串中的每个空格替换成“%20”
class Solution(object):

    def __init__(self):
        pass

    def replaceSpace(self,string):
        resStr = []
        for i in range(0,len(string)):
            if string[i] == ' ':
                resStr.append("02%")
            else:
                resStr.append(string[i])
        # for i in range(len(string)-1,-1,-1):
        #     if string[i] == ' ':
        #         resStr.append("02%")
        #     else:
        #         resStr.append(string[i])
        return "".join(resStr)

if __name__ == '__main__':
    string = "We are Happy"
    solution = Solution()
    res = solution.replaceSpace(string)
    print(res)