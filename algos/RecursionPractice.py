#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.11.7 11:01
'''
递归实战
'''
import logging
class recursion:
    def __init__(self):
        pass

    def factorial(self,n):
        if n == 1:
            return 1
        return n*self.factorial(n-1)


    def FibonacciSequence(self,n):
        if(n==1 or n==2):
            return 1
        return self.FibonacciSequence(n-1) + self.FibonacciSequence(n-2)

    def getYanghuiValues(self,x,y):
        if (y<=x and y>=0):
            if (y==0 or x==y):
                return 1
            else:
                return self.getYanghuiValues(x-1,y-1) + self.getYanghuiValues(x-1,y)
        return -1
    """
    汉诺塔问题：古代有一个梵塔，塔内有三个座A、B、C，A座上有64个盘子，盘子大小不等，大的在下，小的在上。
    有一个和尚想把这64个盘子从A座移到C座，但每次只能允许移动一个盘子，并且在移动过程中，3个座上的盘子始终保持大盘在下， 
    小盘在上。在移动过程中可以利用B座。要求输入层数，运算后输出每步是如何移动的。
    """
    def HanoiRowerMoveDish(self,level,from1,inter,to):
        """
        在程序中，我们把最上面的盘子称为第一个盘子，把最下面的盘子称为第N个盘子
        :param level: 盘子的个数
        :param from1: 盘子的初始地址
        :param inter: 转移盘子的中转部分
        :param to: 盘子的目的地址
        :return:
        """
        # 定义递归终止条件
        if level==1:
            print("从" + str(from1) + " 移动盘子" + str(level) + " 号到" + str(to))
        else:
            # 递归调用，把level-1个盘子从from到inter。
            # 从第N个盘子递归找到最上面的盘子，然后挪到B上。
            self.HanoiRowerMoveDish(level-1,from1,to,inter)
            print("从" + str(from1) + " 移动盘子" + str(level) + " 号到" + str(to))

            self.HanoiRowerMoveDish(level-1,inter,from1,to)

    def getBinaryTreeDepth(self,tree):
        if tree == None:
            return 0

        left = self.getBinaryTreeDepth(tree.left)
        right = self.getBinaryTreeDepth(tree.right)

        return left +1 if left>right else right+1


if __name__ == '__main__':

    s = recursion()
    s.HanoiRowerMoveDish(10,'A','B','C')





