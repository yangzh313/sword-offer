'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        ou = []
        for i in array:
            if i & 1 == 1:
                odd.append(i)
            elif i & 1 == 0:
                ou.append(i)
        return odd+ou

    def reOrderArray2(self, array):
        one = [x for x in array if x%2==1]
        two = [x for x in array if x%2==0]
        return one + two


    

