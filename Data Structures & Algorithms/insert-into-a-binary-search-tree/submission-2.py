# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        ptr= curr
        while curr:
            if curr.val > val:
                ptr = curr
                curr = curr.left
            elif curr.val <= val:
                ptr = curr
                curr = curr.right
        if ptr.val > val:
            ptr.left = TreeNode(val)
        else:
            ptr.right = TreeNode(val)
        return root