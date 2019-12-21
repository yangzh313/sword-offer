'''
输入一个链表，输出该链表中倒数第k个结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k==0:
            return None
        slow = fast = head        
        for _ in range(k):            
            if not fast:
                return None
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next            
        return slow
            