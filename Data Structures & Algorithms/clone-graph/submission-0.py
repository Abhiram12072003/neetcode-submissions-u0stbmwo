"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        
        q.append(node)

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        while q:
            front = q.popleft()
            for chd in front.neighbors:
                if chd not in oldToNew:
                    oldToNew[chd] = Node(chd.val)
                    q.append(chd)
                oldToNew[front].neighbors.append(oldToNew[chd])
        return oldToNew[node]
            