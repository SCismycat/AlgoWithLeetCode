#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.24 9:22
# 寻找最小的k个数字
import heapq
class Solution(object):
    def __init__(self,k):
        self.k = k
        self.data = []

    def pushData(self,elem):
        if len(self.data) <self.k:
            heapq.heappush(self.data,elem)
        else:
            topSmall = self.data[0]
            if elem<topSmall:
                heapq.heapreplace(self.data,elem)

    def minK(self):
        return [heapq.heappop(self.data) for x in range(len(self.data))]