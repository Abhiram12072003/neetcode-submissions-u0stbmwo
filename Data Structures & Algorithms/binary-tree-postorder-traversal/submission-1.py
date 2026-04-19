# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st = [root]
        st2 = []
        while st:
            tp = st[-1]
            st.pop()
            st2.append(tp.val)
            if tp.left:
                st.append(tp.left)
            if tp.right:
                st.append(tp.right)
        return st2[::-1]