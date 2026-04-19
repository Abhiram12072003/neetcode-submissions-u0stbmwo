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
                curr = st[-1]
                if curr.right and curr.right != prevNode:
                    curr = curr.right
                else:
                    st.pop()
                    if not curr.left and not curr.right and curr.val == target:
                        if not st:
                            return None
                        parent = st[-1]
                        if parent.left == curr:
                            parent.left = None
                        elif parent.right == curr:
                            parent.right = None
                    else:
                        prevNode = curr
                    curr = None
        return root