#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leslee
class Solution(object):
    def combinationSum(self,candidates,target):
        candidates,res,stack,lenth = sorted(set(candidates)),[],[(0,[],target)],len(candidates)
        while stack:
            i,temp,tar = stack.pop()
            while i<lenth and tar>0:
                if candidates[i]==tar : res+=temp+[candidates[i]],
                stack += (i,temp+[candidates[i]],tar-candidates[i]),
                i+=1
        return res
    # def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     candidates, res, stack, lenth = sorted(set(candidates)), [], [(0, [], target)], len(candidates)
    #     while stack:
    #         i, temp, tar = stack.pop()
    #         while i < lenth and tar > 0:
    #             if candidates[i] == tar: res += temp + [candidates[i]],
    #             stack += (i, temp + [candidates[i]], tar - candidates[i]),
    #             i += 1
    #     return res

if __name__ == '__main__':
    candidate = [1,2,3]
    target = 5
    s =Solution()
    result = s.combinationSum(candidate,target)
    print(result)