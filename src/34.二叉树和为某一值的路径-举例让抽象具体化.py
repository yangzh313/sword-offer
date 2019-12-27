'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    # 方法一：iteratively
    def FindPath(self, root, expectNumber):
        # write code here
        stack = root and [(root, [root.val], expectNumber)]
        ans = []
        while stack:
            n, v, t = stack.pop()
            if not n.left and not n.right and n.val==t:
                ans.append(v)
            if n.right:
                stack.append((n.right, v+[n.right.val], t-n.val))
            if n.left:
                stack.append((n.left, v+[n.left.val], t-n.val))
        return ans

    # 方法二：recursively
    def FindPath2(self, root, expectNumber):
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath2(root.left, expectNumber-root.val)
        right = self.FindPath2(root.right, expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)


