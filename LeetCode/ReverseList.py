#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.6 9:34

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self,pHead):
        if pHead == None or pHead.next == None:
            return pHead
        cur = pHead
        newHead = None
        tmp = None

        while cur:
            tmp = cur.next# 去掉当前node，临时链表保存余下的
            # 构造新的反转链表
            cur.next = newHead # 当前节点的下一个赋值给newHead，第一次把none赋值给cur，第二次把当前newHead赋值给cur
            newHead = cur # 不断增加cur的值
            cur = tmp
        return newHead

    # 如果可以修改原链表
    def reverseList_(self,head):
        if not head or not head.next:
            return head

        Node = None
        while head:
            p = head
            head = head.next
            p.next = Node
            Node = p
        return Node

    # 递归实现
    def reverseList_Recurrent(self,head):
        if not head or not head.next:
            return head
        newHead = self.reverseList_Recurrent(head.next)
        head.next.next = head
        head.next = None
        return newHead




    # def reverseList(self,phead):
    #     if phead == None or phead.next == None:
    #         return phead
    #     cur = phead
    #     newHead = None
    #     tmp = None # 用来保存下一个链表，防止找不到下一个节点
    #
    #     while cur:
    #         tmp = cur.next
    #         # 当前节点是cur
    #         cur.next = newHead
    #         newHead = cur # 当前节点是cur
    #         cur = tmp
    #     return newHead