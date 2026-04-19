# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque()
        q.append(root)
        ans = str(root.val) + " "
        while q:
            tp = q.popleft()
            if tp.left:
                ans += (str(tp.left.val) + " ")
                q.append(tp.left)
            if not tp.left:
                ans += "null "
            if tp.right:
                ans += (str(tp.right.val) + " ")
                q.append(tp.right)
            if not tp.right:
                ans += "null "
            # ans += " "
        return ans[:-1]
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lis = data.split(" ")
        print(lis, data)
        n = len(lis)
        if n == 0:
            return None
        i = 1
        node = TreeNode(lis[0])
        q = deque()
        q.append(node)
        while q:
            ptr = q.popleft()
            if i == n:
                break
            if i<n and lis[i] != "null":
                ptr.left = TreeNode(lis[i])
                q.append(ptr.left)
            i += 1
            if i<n and lis[i] != "null":
                ptr.right = TreeNode(lis[i])
                q.append(ptr.right)
            i += 1
        return node