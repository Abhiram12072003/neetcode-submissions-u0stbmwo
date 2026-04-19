# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def func(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False 
        h1 = self.func(p.left, q.left)
        h2 = self.func(p.right, q.right)
        return h1 and h2 and p.val == q.val 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.func(p, q)