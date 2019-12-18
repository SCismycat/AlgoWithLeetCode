#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.18 13:46
from itertools import combinations
def findMaxZuma(lists):
    if lists is None:
        return
    lists_reset = list(set(lists))
    combine_list = combinations(lists_reset,2)
    maxNum = 0
    for tup in combine_list:
        if tup[0]==tup[1]:
            continue
        list1 = [0 for x in range(len(lists))]
        for i in range(len(lists)):
            if lists[i] ==tup[0]:
                list1[i] = 0
            elif lists[i] == tup[1]:
                list1[i] = 0
            else:
                list1[i] = -1
            # p判断首尾

        res= 1
        for i in range(len(list1)-1):
            if list1[i] ==list1[i+1]==0:
                    res+=1
            else:
                continue
        if res>maxNum:
            maxNum = res
    return maxNum
if __name__ == '__main__':
    # BLUE = 0;PURPLR=1;YELLOW=2;GREEN=3;
    lists = [0,0,1,0,0,1,3,1,2,1,2,1,2,3,3,3]
    a = findMaxZuma(lists)
    print(a)