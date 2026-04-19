# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.func(root.left, val)
        else:
            root.right = self.func(root.right, val)
        return root
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.func(root, val)