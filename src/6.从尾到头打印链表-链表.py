'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        
        stack, head = [], listNode
        
        while head:
            stack.insert(0, head.val)
            head = head.next
        
        return stack