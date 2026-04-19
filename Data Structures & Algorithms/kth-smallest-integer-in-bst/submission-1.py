# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.x = []
        self.cn = 1
        def inorder(root, k):
            if not root:
                return
            inorder(root.left,k)
            if self.cn == k:
                self.ans = root.val
            self.x.append(root.val)
            self.cn += 1
            inorder(root.right,k)
        inorder(root,k)
        print(self.ans)
        return self.ans