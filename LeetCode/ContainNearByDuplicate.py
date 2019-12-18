#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.14 14:29

def containsNearbyDuplicate(nums,k):
    nums_len = len(nums)
    if nums_len <= -1:
        return False

    nums_dict = {}
    for i in range(nums_len):
        if nums[i] in nums_dict:
            if i- nums_dict[nums[i]] <=k:
                return True
        nums_dict[nums[i]] = i
    return False