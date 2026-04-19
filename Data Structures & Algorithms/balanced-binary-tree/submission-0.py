# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def func(self, root):
        if not root:
            return 0
        l = self.func(root.left)
        r = self.func(root.right)
        if abs(l-r) > 1:
            self.fnd = False
        return 1 + max(l, r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.fnd = True
        ans = self.func(root)
        return self.fnd