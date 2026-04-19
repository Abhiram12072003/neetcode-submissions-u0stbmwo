# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def func(self, root):
        if not root:
            return float("-inf")
        x = root.val
        p1 = self.func(root.left)
        p2 = self.func(root.right)
        # print(root.val, p1, p2)
        po = [x, x+p1, x+p2, x+p1+p2, self.ans]
        self.ans = max(po)
        # print(po)
        return max(po[:3])
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        sd = self.func(root)
        return self.ans