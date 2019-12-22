'''
输入一个链表，反转链表后，输出新链表的表头。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        
        pre = None

        while pHead:
            temp =pHead.next
            pHead.next = pre
            pre = pHead
            pHead = temp
        return pre

    def ReverseList2(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        pre = None
        while pHead:
            pHead.next, pre, pHead = pre, pHead, pHead.next
        return pre