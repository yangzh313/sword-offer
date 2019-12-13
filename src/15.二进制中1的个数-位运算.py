'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n:
            count += 1
            n = (n-1) & n
        
        return count
    
    def NumberOf1_2(self, n):
        count = 0
        for _ in range(32):
            count += (n&1==1)
            n >>= 1
        return count   

    def NumberOf1_3(self, n):
        return sum([(n>>i & 1) for i in range(0, 32)])     
            
