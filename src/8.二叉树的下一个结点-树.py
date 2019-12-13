'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
             return None
        # 有右子树，右子树中最左节点
        if pNode.right:
            pre = pNode.right
            while pre.left:
                pre = pre.left
            return pre.val
        while pNode.next:
            tmp = pNode.next
            if tmp.left==pNode:
                return tmp
            pNode = tmp
