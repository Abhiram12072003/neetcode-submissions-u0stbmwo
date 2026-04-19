# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        d = {}
        for id, val in enumerate(inorder):
            d[val] = id
        def dfs(l, r):
            if l > r:
                return None
            node = TreeNode(preorder[self.idx])
            index = d[preorder[self.idx]]
            self.idx += 1
            node.left = dfs(l, index-1)
            node.right = dfs(index+1, r)
            return node
        return dfs(0, len(inorder)-1)
            