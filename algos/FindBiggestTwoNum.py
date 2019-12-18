#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.15 9:20


def find_max_two_num(li):
    fMax = 0
    sMax = 0
    for num in li:
        if num>fMax:
            sMax = fMax
            fMax = num
        elif num>sMax:
            sMax = num


