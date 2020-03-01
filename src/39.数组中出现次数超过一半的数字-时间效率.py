'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# 思路1：对数组排序，找数组中间的数
def MoreThanHalfNum_Solution(self, numbers):
    numbers.sort()
    numMid = numbers[len(numbers)/2]
    if numbers.count(numMid)>len(numbers)/2:
        return numMid
    else:
        return 0

# 思路2：如果有符合条件的数字，则它出现的次数比其他所有数字出现的次数和还要多。
# 在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。然后再判断它是否符合条件即可。
# 这实际上就是“分形叶”法，对数组同时去掉两个不同的数字，到最后剩下的一个数就是该数字。如果剩下两个，那么这两个也是一样的，就是结果，在其基础上把最后剩下的一个数字或者两个回到原来数组中，将数组遍历一遍统计一下数字出现次数进行最终判断。
def MoreThanHalfNum_Solution2(self, numbers):
    if not numbers:
        return 0
    res = numbers[0]
    times = 1
    length = len(numbers)
    for i in range(1, length):
        if times == 0:
            res = numbers[i]
            times = 1
        elif res == numbers[i]:
            times += 1
        else:
            times -= 1
    import collections
    return res if collections.Counter(numbers)[res]>length/2 else 0