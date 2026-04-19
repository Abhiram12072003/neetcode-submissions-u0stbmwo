# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstDelete(self, root, key):
        if not root:
            return None
        if root.val < key:
            root.right = self.bstDelete(root.right, key)
        elif root.val > key:
            root.left = self.bstDelete(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            curr = root.right
            while curr.left:
                curr = curr.left
            curr.left = root.left
            res = root.right
            del root
            return res
        return root



    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # return self.bstDelete(root, key)
        parent = None
        curr = root
        while curr and curr.val != key:
            parent = curr
            if curr.val < key:
                curr = curr.right
            else:
                curr = curr.left
        if not curr:
            return root
        if not curr.left or not curr.right:
            chd = curr.left if curr.left else curr.right
            if not parent:
                return chd
            elif parent.left == curr:
                parent.left = chd
            else:
                parent.right = chd
        else:
            nodeToDel = curr
            par = None
            curr = curr.right
            while curr.left:
                par = curr
                curr = curr.left
            if par:
                # do it
                par.left = curr.right
                curr.right = par
            curr.left = nodeToDel.left
            if not parent:
                return curr
            elif parent.left == nodeToDel:
                parent.left = curr
            else:
                parent.right = curr
        return root