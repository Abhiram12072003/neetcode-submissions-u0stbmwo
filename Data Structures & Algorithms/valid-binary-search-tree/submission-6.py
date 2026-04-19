# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def func(self, root, mn, mx):
        if not root:
            return True
        if mn>=root.val or root.val>=mx:
            return False
        return self.func(root.left, mn, max(mn, root.val)) and self.func(root.right, min(mx,root.val), mx)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.func(root, float("-inf"), float("inf"))