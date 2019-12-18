#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.12 16:31
from collections import Counter
def majorityElementByCounter(nums):
    data = Counter(nums)
    result = []
    for k,v in data.items():
        result.append(k)
    return result[0]

# 因为众数是在n/2,所以排序后一定在n/2是众数。
# 投票算法
def majorityElement(nums):
    count = 1
    maj = nums[0]
    for i in range(len(nums)):
        if maj == nums[i]:
            count+=1
        else:
            count -=1
            if count ==0:
                maj = nums[i+1]
    return maj

# 暴力求解法
def majorityElem(nums):
    maj_count = len(nums)//2
    for num in nums:
        count = sum(1 for elem in nums if elem==maj_count)
        if count > maj_count:
            return num

# hash表：
# 出现次数最多的元素大于n/2次，所以可以用哈希表快速统计每个元素出现次数
def majorityElemHashTable(nums):
    count = dict()
    for num in nums:
        if num not in count.keys():
            count[num] = 1
        else:
            count[num] = count.get(num)+1
    return count
    # 遍历上面的count取值即可
#  排序取下标，因为限定了众数一定是大于n/2的
def majorityElemBySort(nums):
    maj_nums = sorted(nums)
    return nums[len(nums)//2]

# 分治
# 如果知道了左边一半和右边一般的众数，就可以知道全局众数

# 投票算法






if __name__ == '__main__':
    l = [2,2,1,1,1,2,2]
    print(majorityElement(l))