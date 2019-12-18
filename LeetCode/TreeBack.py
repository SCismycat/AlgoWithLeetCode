#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Leslee

class Solution(object):
    res = []
    def back_track(self,candidate,target,start,val):
        if target == 0:
            Solution.res.append(val)
        else:
            for i in range(start,len(candidate)):
                if target < 0:
                    break
                new_val = val+[candidate[i]]
                target = target-candidate[i]
                self.back_track(candidate,target,i,new_val)

    def combinationSum(self,candidate,target):

        self.back_track(candidate,target,0,[])
        return Solution.res

if __name__ == '__main__':
    candidate = [1,2,3]
    target = 5
    s =Solution()
    result = s.combinationSum(candidate,target)
    print(result)



