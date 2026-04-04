class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        node = Trie()
        n, m = len(board), len(board[0])
        
        for i in range(len(words)):
            word = words[i]
            ptr = node
            for char in word:
                if char not in ptr.children:
                    ptr.children[char] = Trie()
                ptr = ptr.children[char]
            ptr.end = True
        
        curr = node
        ans = set()

        def find(curr, i, j, si):
            if i>=n or j>=m or i<0 or j<0:
                return
            
            if board[i][j] not in curr.children or visited[i][j]:
                return

            visited[i][j] = True
            
            curr = curr.children[board[i][j]]
            
            si += board[i][j]

            if curr.end:
                ans.add(si)
            
            find(curr, i+1, j, si)
            find(curr, i-1, j, si)
            find(curr, i, j+1, si)
            find(curr, i, j-1, si)

            visited[i][j] = False
            
            return
        
        visited = [[False]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                # visited = [[False]*m for i in range(n)]
                find(curr, i, j, "")
        
        return list(ans)