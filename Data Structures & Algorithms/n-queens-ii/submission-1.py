class Solution:
    def totalNQueens(self, n: int) -> int:
        pos = set()
        neg = set()
        col = set()
        def func(itr):
            if itr == n:
                return 1

            res = 0
            for j in range(n):
                
                flag = False


                if j in col or (itr+j) in pos or (itr-j) in neg:
                    continue
                col.add(j)
                pos.add(itr+j)
                neg.add(itr-j)
                res += func(itr+1)
                col.remove(j)
                pos.remove(itr+j)
                neg.remove(itr-j)
            return res
        
                  
        return func(0)


