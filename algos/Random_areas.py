#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.15 13:33
import random
# 给定一个1-5的函数，随机生成1-7的函数
def random7():
    a = random.randint(0,5)-1
    b = random.randint(0,5)-1
    num = 5*a +b
    if(num>20):
        return random7()
    else:
        return num % 7 + 1