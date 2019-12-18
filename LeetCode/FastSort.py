#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.6 10:51

def quick_sort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less_pivot = [x for x in array if x<=pivot]
        more_pivot = [x for x in array if x>pivot]
        return quick_sort(less_pivot) + [pivot] + quick_sort(more_pivot)

def parition(arr,low,high):
    i = (low-1)
    pivot = arr[high]# 选最后一个的一个当阈值
    for j in range(low,high):
        # 如果当前元素小于等于基准值
        if arr[j]<=pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] # 当前元素和第i(i从零开始)个元素交换位置，排序
    arr[i+1],arr[high] = arr[high],arr[i+1]# 交换元素位置
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pi = parition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


# 冒泡排序
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

