# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def find(root, hgt = 0):
            if not root:
                # ans = max(ans, hgt)
                return 0
            x1 = find(root.left, hgt)
            x2 = find(root.right, hgt)
            self.ans = max(self.ans, x1 + x2)
            return 1 + max(x1, x2)
        find(root)
        return self.ans