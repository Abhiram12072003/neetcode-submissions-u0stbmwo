"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if not node:
        #     return None
        # q = deque()
        # q.append(node)
        # ptr = Node(node.val)
        # hm = {}
        # hm[node] = ptr
        # while q:
        #     top = q.popleft()
        #     for child in top.neighbors:
        #         if child not in hm:
        #             hm[child] = Node(child.val)
        #             q.append(child)
        #         hm[top].neighbors.append(hm[child])
        oldToNew = {}
        # print(node.val)
        def dfs(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]

            curr = Node(node.val)
            
            oldToNew[node] = curr

            for chd in node.neighbors:
                # if chd not in oldToNew:
                oldToNew[node].neighbors.append(dfs(chd))

            return curr
        
        ptr = dfs(node)    
        
        return ptr