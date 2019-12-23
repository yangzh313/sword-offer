'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # recursively
        def symmetrical(p1, p2):
            if p1 and p2:
                return (p1.val == p2.val and symmetrical(p1.left, p2.right) and
                        symmetrical(p1.right, p2.left))
            else:
                return p1 is p2
            
        if not pRoot:
            return True
        return symmetrical(pRoot.left, pRoot.right)
    
    def isSymmetrical2(self, pRoot):
        # iteratively
        stack = pRoot and [(pRoot.left, pRoot.right)]
        while stack:
            p1, p2 = stack.pop()
            if not p1 and not p2: continue
            if not p1 or not p2: return False
            if p1.val != p2.val: return False
            stack.append((p1.left, p2.right))
            stack.append((p1.right, p2.left))
        return True