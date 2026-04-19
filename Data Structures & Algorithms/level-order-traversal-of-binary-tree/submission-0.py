from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append([root, 0])
        ans = []
        x = []
        x.append(root.val)
        prevLev = -1
        while q:
            ptr, lev = q.popleft()
            if prevLev != lev:
                ans.append(x)
                x = []
                prevLev = lev
            if ptr.left:
                q.append([ptr.left, lev+1])
                x.append(ptr.left.val)
            if ptr.right:
                q.append([ptr.right, lev+1])
                x.append(ptr.right.val)
            print(prevLev, lev)
        return ans