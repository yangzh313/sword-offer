'''
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        if length == 1:
            return rotateArray[0]
        index1, index2 = 0, length-1    
        
        while index1 <= index2:
            middle = (index1 + index2) // 2
            if rotateArray[middle] > rotateArray[index2]:
                index1 = middle + 1
                
            elif rotateArray[middle] < rotateArray[index2]:
                index2 = middle
            else:
                index2 -= 1
            if index1 >= index2:
                break
        return rotateArray[index1]

'''
说明：通过一个递增数组旋转后的数组，找出最小元素。
思路：通过二分法不断缩小范围，由于mid是整除，最后l==mid，
并且nums[mid] > nums[r]的。
'''
class Solution:
    def find_min(nums):
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > nums[l]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid
            else:
                return nums[r]    
