#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.15 10:25

def get_index(lists,target):
    low,high = 0,len(lists)
    while low<high:
        mid = (low+high)//2
        if lists[mid] ==target:
            return mid
        elif lists[mid]<target:
            low = mid+1
        else:
            high = mid
    return -1;