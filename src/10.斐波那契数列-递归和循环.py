'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项
（从0开始，第0项为0）。n<=39
'''

# -*- coding:utf-8 -*-


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        fibNMinusOne = 1
        fibNMinusTwo = 0
        fibN = 0
        for i in range(2, n+1):
            fibN = fibNMinusOne + fibNMinusTwo
            fibNMinusTwo = fibNMinusOne
            fibNMinusOne = fibN
        return fibN


'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶
总共有多少种跳法（先后次序不同算不同的结果）。
'''

# -*- coding:utf-8 -*-


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        floor1 = 1
        floor2 = 2
        floorn = 0
        for _ in range(3, number+1):
            floorn = floor1 + floor2
            floor1 = floor2
            floor2 = floorn
        return floorn

    def jumpFloor2(self, number):
        # write code here
        a = 1
        b = 1
        for i in range(number):
            a, b = b, a+b
        return a

'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
# -*- coding:utf-8 -*-


class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1

        fNMinusOne = 1
        fN = 0
        for _ in range(2, number+1):
            fN = 2 * fNMinusOne

            fNMinusOne = fN
        return fN

    def jumpFloorII(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        s = []
        s.append(1)
        s.append(2)
        for _ in range(2, number):
            s.append(sum(s)+1)
        return s[-1]

'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        fibNMinusOne = 1
        fibNMinusTwo = 1
        fibN = 0
        for i in range(2, number+1):
            fibN = fibNMinusOne + fibNMinusTwo
            fibNMinusTwo = fibNMinusOne
            fibNMinusOne = fibN
        return fibN