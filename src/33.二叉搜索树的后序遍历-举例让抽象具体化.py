'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        l = len(sequence)
        if not sequence or l <= 0:
            return False
        root = sequence[-1]
        
        for i in range(l):
            if sequence[i] > root:
                break
        
        for j in range(i, l):
            if sequence[j] < root:
                return False
            
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < l - 1:
            right = self.VerifySquenceOfBST(sequence[i:l-1])
        return left and right

# 33_1 二叉树的后序遍历
# 方法一：根右左，再倒序。
def postorder_traversal(root):
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res[::-1]
