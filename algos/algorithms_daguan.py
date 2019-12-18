#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.17 9:16
# 找到最大的两个数，一种排序切片，一种比较
def findSecondNumber(lists):
    fNum = 0
    sNum = 0
    if lists is None:
        return
    for num in lists:
        if num>fNum:
            sNum = fNum
            fNum = num
        elif num >sNum:
            sNum = num
    return fNum,sNum

def findSecondNumberSort(lists):
    list1 = sorted(lists)
    return list1[-2:]

# 给定一个有序数组，如[1,2,35,6,11,33],求指定值的下标，二分查找
def findNumberIdx(lists,target):
    low,high = 0,len(lists)
    while(low<high):
        midNumber = (low+high)//2
        if lists[midNumber] == target:
            return midNumber
        elif lists[midNumber]<target:# 目标值比中间值大，在右侧区间，low=mid+1
            low = midNumber+1
        else:
            high = midNumber

# 给定一个字符串去除字符串开头结尾中的空格，字符中间的多个空格转换成一个空格
def deleteBlank(string):
    resultString = ''
    isFirstBlank = False
    for i in range(len(string)):
        if(string[i] == ' ' or string[i]=='\t'):
            if(not isFirstBlank):
                resultString+=string[i]
                isFirstBlank = True
        else:
            resultString+=string[i]
            isFirstBlank = False
    return resultString

# 合并两个有序链表，去重
class ListNode(object):
    def __init__(self,x):
        self.x = x
        self.next = None
    def combineTwoLists(self,list1,list2):
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1
        result = ListNode(0)
        if list1.x < list2.x:
            list1.next = self.combineTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.combineTwoLists(list1,list2.next)
            return list2

# 最大子区间和
def maxAreasSum(lists):
    oneSum = 0
    maxSum = lists[0]
    for i in range(len(lists)):
        oneSum += lists[i]
        maxSum = max(maxSum,oneSum)
        if oneSum<0:
            oneSum = 0
    return maxSum
# 动态规划解法
def maxSum(l1):
    # 每次求和假设已经取得了最大值，所以不用重复计算，直接复制给当前相加的值动态计算下去
    for i in range(1,len(l1)):
        maxSum = max(l1[i]+l1[i-1],l1[i])
        l1[i] = maxSum
    return max(l1)

import random
def random10():
    a = random.randint(0,7)-1
    b = random.randint(0,7)-1
    sum = 7*a+b
    if(sum>40):
        random10()
    else:
        return sum % 7 +1
# 海量数据TopK
import heapq
class TopKHeap(object):
    def __init__(self,x):
        self.x = x
        self.data = []

    def push(self,elem):
        if len(self.data)<self.x:
            heapq.heappush(elem)
        else:
            topk_small = heapq[0]
            if elem>topk_small:
                heapq.heapreplace(elem)
    def topK(self):
        return [x for x in reversed(heapq.heappop(self.data) for x in range(len(self.data)))]
# python 实现二叉树
class Node(object):
    # 先定义节点类
    def __init__(self,elem=-1,lChild=None,rChild=None):
        self.elem = elem
        self.lChild = lChild
        self.rChild = rChild
class binaryTree(object):
    # 二叉树类
    def __init__(self):
        self.root = Node
        self.myQueue = []
    def addNumber(self,elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)# 如果该节点存在右子树，就抛弃

if __name__ == '__main__':
    lists = [1,3,2,4,5,3,2]
    a = findSecondNumber(lists)
    # print(a)
    # b = findSecondNumberSort(lists)
    # print(b)
    # test = "abc    d d e e"
    # a = deleteBlank(test)
    # print(a)
    # li = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # maxSum = maxSum(li)
    # print(maxSum)
    print(random10())