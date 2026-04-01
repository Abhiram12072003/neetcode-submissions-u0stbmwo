class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []
        def func(itr):
            if itr == n:
                return 1

            res = 0
            for j in range(n):
                flag = False
                for id1,jd1 in ans:
                    if abs(itr-id1) == abs(j-jd1) or itr == id1 or jd1 == j:
                        flag = True
                        break

                if not flag:
                    ans.append([itr, j])
                    res += func(itr+1)
                    ans.pop()
            return res
        
                  
        return func(0)


