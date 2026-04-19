# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root):
        if not root:
            return [0,0]
        p1 = self.func(root.left)
        p2 = self.func(root.right)
        return [root.val+p1[1]+p2[1], max(p1)+max(p2)]
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.func(root))