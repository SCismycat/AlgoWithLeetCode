#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.15 10:32

# 合并两个有序链表
# 先定义一个链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self,l1,l2):
        if l1 ==None:
            return l2
        elif l2 == None:
            return l1
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2