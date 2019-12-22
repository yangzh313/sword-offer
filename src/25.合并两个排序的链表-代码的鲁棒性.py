'''
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        pMergeNode = None
        if pHead1.val < pHead2.val:
            pMergeNode = pHead1
            pMergeNode.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeNode = pHead2
            pMergeNode.next = self.Merge(pHead1, pHead2.next)
        return pMergeNode