'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def detectCycle(self, pHead):
    fast = slow = pHead
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break
        else:
            return None
    
    while head is not slow:
        head, slow = head.next, slow.next
    return head




class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)
        if not meetingNode:
            return None
        nodesInLoop = 1
        pNode1 = meetingNode
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            nodesInLoop += 1
        
        pNode1 = pHead
        for i in range(nodesInLoop):
            pNode1 = pNode1.next
        
        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1

    def MeetingNode(self, pHead):
        # write code here
        if not pHead:
            return None
        slow = pHead.next
        if not slow:
            return None
        fast = slow.next
        
        while fast and slow:
            if fast == slow:
                return fast
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return None
            
        
