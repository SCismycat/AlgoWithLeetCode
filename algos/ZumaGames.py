#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.29 15:19

def findMaxSubString(zumaList):
    maxSum = 0
    countList = countSubStringLength(zumaList)
    isEnd = True
    for i in range(3,len(countList)+3):
        while(isEnd):
            if countList[-1][0] != countList[0][0]:
                maxSum = countList[-1][1]+countList[0][1]
                if countList[1][0] == countList[-1][0]:
                    maxSum += countList[1][1]
                    if countList[0][0] == countList[2][0]:
                        maxSum += countList[2][1]
            isEnd = False
        if i<len(countList) and countList[i][0] != countList[i-1][0]:
            sum = countList[i][1] + countList[i-1][1]
            if i<len(countList) and countList[i][0] == countList[i-2][0]:
                sum = sum + countList[i-2][1]
                if countList[i-1][0] == countList[i-3][0]:
                    sum += countList[i-3][1]
            if sum >maxSum:
                maxSum = sum
    return maxSum

def countSubStringLength(zumaList):
    countList = []
    j = 1
    for i in range(1,len(zumaList)+1):
        if i < len(zumaList) and zumaList[i] == zumaList[i-1]:
            j+=1
        else:
            countList.append((zumaList[i-1],j))
            j = 1

    return countList
if __name__ == '__main__':
    # BLUE = 0;PURPLR=1;YELLOW=2;GREEN=3;
    lists = [0,0,1,0,0,1,1,1,1,1,2,1,2,3,3,3]
    a = findMaxSubString(lists)
    print(a)