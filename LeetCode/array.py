#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leslee
from math import floor


class Solution:
    def binary_search(self, nums, low, high, target):
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[high]:
            if nums[mid] < target and target < nums[high]:
                return self.binary_search(nums, mid + 1, high, target)
            else:
                return self.binary_search(nums, low, mid - 1, target)
        else:
            if nums[low] <= target and target < nums[mid]:
                return self.binary_search(nums, low, mid - 1, target)
            else:
                return self.binary_search(nums, mid + 1, high, target)
    def search(self, nums, target) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

if __name__ == '__main__':
    l = [3,5,1]
    s =Solution()
    print(s.search(l, 3))