#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.15 11:46
import heapq

class TopKHeap(object):
    def __init__(self,k):
        self.k = k
        self.data = []

    def push(self,element):
        # 如果最小堆大小不够，就往堆里增加数据
        if len(self.data)<self.k:
            heapq.heappush(self.data,element)
        else:
            # 取堆里最小的数据作为比较对象
            topk_small = self.data[0]
            # 如果元素比堆里数据大，就替换元素为新的堆数据
            if element>topk_small:
                heapq.heapreplace(self.data,element)
    def TopK(self):
        # 从堆中压出topk个数字
        return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]
if __name__ == '__main__':
    alist = [1,43,24,53,4,5,8,4,6,776]
    th = TopKHeap(3)
    for i in alist:
        th.push(i)
    print(th.TopK())
    print(sorted(alist, reverse=True)[0:3])
