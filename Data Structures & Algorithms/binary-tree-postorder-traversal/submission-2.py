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
        st = []
        curr = root
        ans = []
        prevNode = None
        while curr or st:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                ptr = st[-1]
                if ptr.right and ptr.right != prevNode:
                    curr = ptr.right
                else:
                    st.pop()
                    prevNode = ptr
                    ans.append(ptr.val)
        return ans