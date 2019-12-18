#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leslee

class Solution(object):

    def binary_search(self,nums,start,end,target):
        if start>end:
            return -1
        mid = (end - start)//2 + start
        if nums[mid]> target:
            return self.binary_search(nums,start,mid-1,target)
        if nums[mid] < target:
            return self.binary_search(nums,mid+1,end,target)
        return mid


    def searchRange(self,nums,target):
        if len(nums)==0:
            return [-1,-1]
        elif target<nums[0] or target>nums[-1]:
            return [-1,-1]
        else:
            start, end = 0,len(nums)-1
            while start<=end:
                mid = (start+end)//2
                if target>nums[mid]:
                    start = mid+1
                elif target<nums[mid]:
                    end = mid-1
                elif target ==nums[mid]:
                    start = end = mid
                    while start-1>=0 and nums[start-1] == target:
                        start -=1
                    while end + 1 <= len(nums)-1 and nums[end+1]==target:
                        end +=1
                    return [start,end]
        return [-1,-1]







if __name__ == '__main__':

    nums = [1,4]
    s = Solution()
    res = s.searchRange(nums, 4)
    print(res)