#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.29 13:47
from collections import Counter
import re


class Solution(object):
    def __init__(self):
        self.cache = dict()

    def findMinStep(self,board,hand):
        if not board:
            return 0
        if not hand:
            return -1
        if board in self.cache:
            return self.cache[board]
        cnt = Counter(hand)
        size = len(hand)
        ans = -1
        num = 0
        for x in range(1,len(board)+1):
            if x<len(board) and board[x] ==board[x-1]:
                num +=1
            else:
                if cnt[board[x-1]]+num>1:
                    step = max(0,2-num)
                    cnt[board[x-1]] -= step
                    nhand = ''.join(k*v for k,v in cnt.items())
                    nboard = self.simplify(board[:x-num-1]+board[x:])
                    nans = self.findMinStep(nboard,nhand)
                    cnt[board[x-1]] += step
                    if nans != -1 and (ans==-1 or nans + step <ans):
                        ans = nans + step
                num = 0
        self.cache[board] = ans
        return ans
    def simplify(self, param):
        ptn = r'R{3,}|Y{3,}|B{3,}|G{3,}|W{3,}'
        while re.search(ptn,param):
            param = re.sub(ptn,'',param)
        return param

if __name__ == '__main__':
    s = Solution()
    board = 'WWRRBBWW'
    hand = 'WRBRW'
    print(s.findMinStep(board,hand))