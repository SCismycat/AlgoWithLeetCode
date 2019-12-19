#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 22:38
# @Author  : Leslee
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序

def moveZeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    while(j<len(nums)):
        nums[j] = 0
        j += 1
    return nums

if __name__ == '__main__':
    a = [0,1,0,3,12]
    print(moveZeros(a))