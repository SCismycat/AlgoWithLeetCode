#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 22:04
# @Author  : Leslee
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。


def missNumber(nums):
    nums = sorted(nums)
    if nums[len(nums)-1] != len(nums):
        return len(nums)
    elif nums[0] != 0:
        return 0
    for i,j in enumerate(nums):
        if i != j:
            return i
    return -1
if __name__ == '__main__':
    a = missNumber([1])
    print(a)

