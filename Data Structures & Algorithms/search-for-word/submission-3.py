class Solution:
    def func(self, board, i, j, itr, word, vis):
        if itr == len(word):
            self.ans = True
            return
        if i<0 or i==len(board) or j<0 or j==len(board[0]):
            return
        if vis[i][j]:
            return
        # print(i, j, itr)
        if word[itr] != board[i][j]:
            return
        # print(i, j, board[i][j])
        vis[i][j] = True
        self.func(board, i-1, j, itr+1, word, vis)
        self.func(board, i+1, j, itr+1, word, vis)
        self.func(board, i, j-1, itr+1, word, vis)
        self.func(board, i, j+1, itr+1, word, vis)
        vis[i][j] = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        self.ans = False
        vis = []
        for i in range(n):
            xi = [False]*m
            vis.append(xi[:])
        
        vis[0][0] = True
        # print(vis)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    self.func(board, i, j, 0, word, [[False]*m for _ in range(n)])
                if self.ans:
                    break
        
        return self.ans