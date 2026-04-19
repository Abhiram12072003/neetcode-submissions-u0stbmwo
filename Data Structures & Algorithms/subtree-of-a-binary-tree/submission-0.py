# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def fnd2(self, root, subroot):
        if not root and not subroot:
            return True
        if (root and not subroot) or (not root and subroot):
            return False
        x1 = self.fnd2(root.left, subroot.left)
        x2 = self.fnd2(root.right, subroot.right)
        return x1 and x2 and root.val == subroot.val
    
    def fnd(self, root, subroot):
        if not root:
            return
        self.fnd(root.left,subroot)
        self.fnd(root.right, subroot)
        if(root.val == subroot.val):
            if not self.x:
                self.x = self.fnd2(root, subroot)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.x = False
        self.fnd(root, subRoot)
        return self.x