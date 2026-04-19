# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def fnd(root, val):
            if not root:
                return None
            fnd(root.left, max(root.val, val))
            fnd(root.right, max(root.val, val))
            if root.val >= val:
                self.ans += 1
        fnd(root,root.val)
        return self.ans
