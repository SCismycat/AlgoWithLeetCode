#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leslee
class Solution:
    def binary_search(self, nums, start, end, target):
        mid = (end-start) // 2 + start
        if nums[mid] == target:
            return mid
        if start>=end:
            return -1
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, end, target)
        elif nums[mid] > target:
            return self.binary_search(nums, start, mid - 1, target)


    def searchRange(self, nums, target):

        if (len(nums) == 0):
            return [-1, -1]
        index = self.binary_search(nums, 0, len(nums), target)
        first = 0
        second = index
        if (index == -1):
            return [-1, -1]
        else:
            for i in range(index, 0):
                i -= 1
                if nums[i] != target:
                    first = i + 1
                    break
            for j in range(len(nums), index + 1):
                if nums[j] != target:
                    second = j - 1
                    break
                else:
                    second += 1
        return [first, second]

if __name__ == '__main__':
    nums = [2,3,4,6,7,8,8,10]
    s = Solution()

    res =  s.searchRange(nums,8)
    print(res)









