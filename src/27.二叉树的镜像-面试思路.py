'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return root
        if not root.left and not root.right:
            return root
        pTemp = root.left
        root.left = root.right
        root.right = pTemp
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)

    def Mirror2(self, root):
        stack = root and [root]
        while stack:
            n = stack.pop()
            if n:
                n.left, n.right = n.right, n.left
                stack += n.right, n.left
