#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.11 11:30
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

def generate(numRows):
    yang_list = []
    for i in range(numRows):
        now_list = [1]*(i+1)# 构建一个全1的数组
        if i >=2:
            # 修改全1数组
            for n in range(1,i):
                now_list[n] = pre[n-1] + pre[n]
        yang_list.append(now_list)
        pre = now_list
    return yang_list

# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
def generate_idx(numRows):
    yang_list = []
    for i in range(numRows+1):
        now_list = [1]*(i+1)# 构建一个全1的数组
        if i >=2:
            # 修改全1数组
            for n in range(1,i):
                now_list[n] = pre[n-1] + pre[n]
        yang_list.append(now_list)
        pre = now_list
    return yang_list[-1]

if __name__ == '__main__':
    print(generate(5))