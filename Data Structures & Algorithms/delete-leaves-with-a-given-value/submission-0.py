# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root, target):
        if not root:
            return None
        root.left = self.func(root.left, target)
        root.right = self.func(root.right, target)
        if root.val == target and not root.left and not root.right:
            return None
        return root

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.func(root,target)