#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.21 11:05
# # 编写一个函数来查找字符串数组中的最长公共前缀
class Solution(object):
    def __init__(self):
        pass

    def longestCommonPrefix(self,lists):
        if(lists ==None or len(lists)==0):
            return ""
        lists = sorted(lists)
        firstString = lists[0]
        lastString = lists[-1]
        resPrefix = []
        if len(firstString)>=len(lastString):
            for i in range(len(lastString)):
                if(firstString[i] == lastString[i]):
                    resPrefix.append(firstString[i])
                else:
                    break
        elif len(firstString)<len(lastString):
            for i in range(len(firstString)):
                if(firstString[i]==lastString[i]):
                    resPrefix.append(firstString[i])
                else:
                    break
        return "".join(resPrefix)


if __name__ == '__main__':
    li = ["flower","flow","flight"]
    s = Solution()
    res = s.longestCommonPrefix(li)
    print(res)
