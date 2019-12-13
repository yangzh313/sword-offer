'''
题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，
n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，
此时得到的最大乘积是18。
'''

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        # 动态规划
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 1
        if number == 3:
            return 2
        
        products = [0, 1, 2, 3]
        
        for i in range(4, number+1):
            max = 0
            for j in range(1, i//2+2):
                product = products[j] * products[i-j]
                if max < product:
                    max = product
            products.append(max)
        
        return products[-1]


    def cutRope_2(self, number):
        # 贪婪算法
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2

        # 尽可能多地减去长度为3地绳子段
        timesOf3 = number // 3

        # 当绳子最后剩下为长度4地时候，不能再减去3地绳子
        if number - timesOf3*3 == 1:
            timesOf3 -= 1

        timesOf2 = (number - timesOf3*3)//2
        return pow(3, timesOf3)*pow(2, timesOf2)

