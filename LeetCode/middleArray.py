#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leslee
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if (len(nums1) == 0):
            length = len(nums2) % 2
            if (length == 0):
                return (nums2[round(len(nums2) / 2-0.3)] + nums2[round(len(nums2) / 2-0.7)]) / 2.0
            else:
                return nums2[len(nums2) // 2 ]
        elif (len(nums2) == 0):
            length1 = len(nums1) % 2
            if (length1 == 0):
                print((nums1[round(len(nums1) / 2-0.3)] + nums1[round(len(nums1) / 2-0.7)]) / 2.0)
                return (nums1[round(len(nums1) / 2-0.3)] + nums1[round(len(nums1) / 2-0.7)]) / 2.0
            else:
                return nums1[len(nums1) // 2 ]

        num = nums1 + nums2
        num = sorted(num)
        if (len(num) == 0):
            return
        else:
            length3 = len(num) % 2
            if (length3 == 0):
                return (num[round(len(num) / 2-0.3)] + num[round(len(num) / 2-0.7)]) / 2.0
            else:
                print(num[len(num) // 2] / 1.0)
                return num[len(num) // 2] / 1.0

if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = []
    solu = Solution()
    solu.findMedianSortedArrays(nums1=nums1,nums2=nums2)