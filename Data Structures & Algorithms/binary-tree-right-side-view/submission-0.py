# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = deque()
        dq.append([root, 0])
        x = []
        x.append(root.val)
        prevLevel = -1
        ans = []
        while dq:
            ptr, lev = dq.popleft()
            # print(ptr.val)
            if prevLevel != lev:
                # print(x)
                ans.append(x[-1])
                x = []
            if ptr.left:
                x.append(ptr.left.val)
                dq.append([ptr.left, lev+1])
            if ptr.right:
                x.append(ptr.right.val)
                dq.append([ptr.right, lev+1])
            prevLevel = lev
        return ans

