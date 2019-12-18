#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.14 9:39
# slice切片
def rotateList(nums,k):
    resultList = nums[k+1::]+nums[0:k+1]
    return resultList

def rotateList1(nums,k):
    length = len(nums)
    k %= length
    for i in range(0,k,1):
        previous = nums[length-1]
        for j in range(0,length-1):
            tmp = nums[j]
            nums[j] = previous
            previous = tmp
    return nums

def reverse(nums,start,end):
    while(start<end):
        tmp = nums[start]
        nums[start] = nums[end]
        nums[end] = tmp
        start +=1
        end -= 1

def retateList2(nums,k):
    llen = len(nums)
    k %= llen
    reverse(nums,0,llen-1)
    reverse(nums,0,k-1)
    reverse(nums,k,llen-1)




if __name__ == '__main__':
    nums = [-1,-100,3,99]
    k = 2
    print(rotateList1(nums,k))