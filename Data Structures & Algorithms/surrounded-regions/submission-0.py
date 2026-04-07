class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        n, m = len(board), len(board[0])
        visited = [[False]*m for i in range(n)]

        def dfs(i, j):
            
            if i<0 or j<0 or i>=n or j>=m or board[i][j] == 'X' or visited[i][j]:
                return
            # print("dfs", i, j)
            visited[i][j] = True
            for dx, dy in directions:
                dfs(i+dx, j+dy)
        
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)
        
        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n-1][j] == 'O':
                dfs(n-1, j)
        # print(visited)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'
        

        