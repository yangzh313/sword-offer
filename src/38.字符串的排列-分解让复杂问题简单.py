'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        # ss=''时，返回的是一个tupple，['']
#         为什么使用set去重，因为当ss='aa'的时候，牛客网的测试用例要求返回一个元素，即['aa']。
# 排序也是为了满足测试用例。
        if not ss:
            return []
        return sorted(list(set([''.join(x) for x in itertools.permutations(ss]))))
