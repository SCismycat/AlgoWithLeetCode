#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.17 11:51

#LCS问题就是求两个字符串最长公共子串的问题。
# 解法就是用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，若是匹配则为1,否则为0。
# 然后求出对角线最长的1的序列，其对应的位置就是最长匹配子串的位置。
def getLcsSubStr(s1,s2):
    m = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)] # 生成0矩阵，比正常列表多1
    mMax = 0 #最长匹配的长度
    p = 0 # 记录最长匹配在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                # 如果两个子串相等，就在对角线上+1.
                m[i+1][j+1] = m[i][j]+1
                # 每次记录mMax最长的长度，如果有比现在最长长度长的就更新mMax；
                if m[i+1][j+1] > mMax:
                    mMax = m[i+1][j+1]
                    p = i+1
    return s1[p-mMax:p],mMax
print(getLcsSubStr('abcdfg','abdfg'))

def findLcsQue(s1,s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，比正常列表多1
    d = [[None for x in range(len(s2)+1)] for x in range(len(s1)+1)] # 记录转移方向
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                m[p1+1][p2+1] = m[p1][p2]+1
                d[p1+1][p2+1] = 'ok'
            elif m[p1+1][p2]>m[p1][p2+1]:
                m[p1+1][p2+1] = m[p1+1][p2]
                d[p1+1][p2+1] = 'left'
            else:
                m[p1+1][p2+1] = m[p1][p2+1]
                d[p1+1][p2] = 'up'
    s = []
    p1,p2 = len(s1),len(s2)
    while m[p1][p2]:
        c = d[p1][p2]
        if c =='ok':
            s.append(s1[p1-1])
            p1-=1
            p2-=1
        if c == 'left':
            p2 -= 1
        if c =='up':
            p1-=1
    s.reverse()
    return "".join(s)

