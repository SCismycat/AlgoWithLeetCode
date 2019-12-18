#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.5 9:49

'''
定义两个序列X、Y，二维数组f[i][j]表示X的i位和Y的j位之前的最长公共子序列长度，
则有
 f[1][1] = same(1,1)
 f[i][j] = max(f[i-1][j-1]+same(i,j),f[i-1][j],f[i][j-1)

其中same(i,j)表示X[i]==Y[j]
 same(a,b)当X的第a位于Y的第b位完全相同时为1，否则为0
 此时，f[i][j]中最大的数便是 X和 Y的最长公共子序列的长度，依据该数组回溯，便可找出最长公共子序列。

如：

X = 'helloword'
Y = 'eoskod'

X，Y的最长公共子序列长度为4，最长公共子序列为'eood'

该算法的空间、时间复杂度均为O(n^2)} O(n^2)。经过优化后，空间复杂度可为 O(n),时间复杂度可为O(nlogn)。
注：最长公共子序列不要求序列连续
'''
UP_LEFT = 0
UP = 1
LEFT = 2


def LCSLength(X,Y):
    m = len(X)
    n = len(Y)
    f = [[0 for x in range(n+1)] for y in range(m+1)]
    # 路径数组
    path = [[-1 for x in range(n+1)] for y in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(X[i-1] == Y[j-1]):
                f[i][j] = f[i-1][j-1] + 1
                path[i][j] = UP_LEFT
            else:
                if f[i-1][j]>f[i][j-1]:
                    f[i][j] = f[i-1][j]
                    path[i][j] = UP
                else:
                    f[i][j] = f[i][j-1]
                    path[i][j] = LEFT
    return f[m][n],path

def getpath(path,X,i,j,arr):
    if i==0 or j ==0:
        return
    elif(path[i][j] == UP_LEFT):
        getpath(path,X,i-1,j-1,arr)
        arr.append(X[i-1])
    elif(path[i][j]==UP):
        getpath(path,X,i-1,j,arr)
    elif(path[i][j]==LEFT):
        getpath(path,X,i,j-1,arr)
    else:
        pass
# X = [1,3,1,4,5]
# Y = [1,1,1,4,5]
X = 'helloword'
Y = 'eoskod'
arr = []
length,path = LCSLength(X,Y)
getpath(path,X,len(X),len(Y),arr)
print(length)
print(arr)

def findLCS(A,n,B,m):
    if m ==0 or n == 0:
        return -1
    c = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1],c[i-1][j])
    return c[-1][-1]# 序列长度

if __name__ == '__main__':
    line = input().split(',')
    A = line[0][1:-1]
    n = int(line[1])
    B = line[2][1:-1]
    m = int(line[-1])
    print (findLCS(A, n, B, m))











