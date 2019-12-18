#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.12 16:16

# 双指针
def twoSum(numbers,target):

    left,right = 0,len(numbers)-1
    while(left<right):
        if numbers[left] + numbers[right] == target:
            return [left+1,right+1]
        elif numbers[left] + numbers[right] <target:
            left +=1
        else:
            right -=1
