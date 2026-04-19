# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # self.ans = 0
        def fnd(root, val):
            if not root:
                return 0
            res = 1 if root.val>=val else 0
            res += fnd(root.left, max(root.val, val))
            res += fnd(root.right, max(root.val, val))
            return res
        return fnd(root,root.val)
