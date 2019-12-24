'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
'''

class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, node):
        # write code here        
        self.stack.append(node)
        if not self.minStack or node <= self.minStack[-1]:
            self.minStack.append(node)
        else:
            self.minStack.append(self.minStack[-1])
    def pop(self):
        # write code here
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minStack[-1]