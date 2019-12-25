'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return [] 
        l = []
        queue = [root]
        while len(queue):
            t = queue.pop(0)
            l.append(t.val)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
        return l

    def PrintFromTopToBottomLevel(self, root):
        ans, level = [], root and [root]
        while level:
            ans.append([n.val for n in level])
            level = [k for n in level for k in (n.left, n.right) if k]
        return ans

    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        ans, level, order = [], root and [root], 1
        while level:
            ans.append([n.val for n in level][::order])
            order *= -1
            level = [k for n in level for k in (n.left, n.right) if k]
        return ans
        