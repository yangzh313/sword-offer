'''
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
保证base和exponent不同时为0
'''

class Solution_1:
    def Power(self, base, exponent):
        # write code here
        if base==0 and exponent==0:
            return 0
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        baseOfEx = 1
        if exponent > 1:
            for _ in range(exponent):
                baseOfEx = baseOfEx * base
        else:
            if base == 0:
                return 0
            else:
                for _ in range(-exponent):
                    baseOfEx = baseOfEx / base
            
        return baseOfEx

class Solution_2:
    def Power(self, base, exponent):
        def pow_with_unsigned(base, exponent):
            if base==0 and exponent==0:
                return 0
            if exponent == 0:
                return 1
            if exponent == 1:
                return base
            result = pow_with_unsigned(base, exponent>>1)
            result *= result
            if exponent & 1 == 1:
                result *= base

            return result
        
        if exponent < 0:
            if base == 0:
                return 0
            else:
                return 1 / pow_with_unsigned(base, -exponent)
        else:
            return pow_with_unsigned(base, exponent)

        