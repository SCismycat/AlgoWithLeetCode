#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 0:17
# @Author  : Leslee


# 冲突检测
def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY - i):
            return True
    return False

# 基线条件
def queens(num,state):
    # 最后一个皇后
    if len(state) == num -1:
        for pos in range(num):
            if not conflict(state,pos):
                yield (pos,)
    else:
        for pos in range(num):
            if not conflict(state,pos):
                for result in queens(num,state+(pos,)):
                    yield (pos,) + result