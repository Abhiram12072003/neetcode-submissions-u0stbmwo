"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            if n == 1:
                return Node(grid[r][c], True)
            mid = n//2
            topleft = dfs(mid,r,c)
            topright = dfs(mid,r,c+mid)
            bottomleft = dfs(mid,r+mid,c)
            bottomright = dfs(mid,r+mid,c+mid)
            if topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val == topright.val and topright.val == bottomleft.val and bottomleft.val == bottomright.val:
                return Node(grid[r][c], True)  
            return Node(0, False, topleft, topright, bottomleft,bottomright)
        return dfs(len(grid), 0, 0)