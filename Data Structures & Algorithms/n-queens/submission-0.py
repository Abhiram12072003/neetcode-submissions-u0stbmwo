class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        answer = []
        def func(itr):
            if itr == n:
                answer.append(ans[:])
                return

            for j in range(n):
                flag = False
                for id1,jd1 in ans:
                    if abs(itr-id1) == abs(j-jd1) or itr == id1 or jd1 == j:
                        flag = True
                        break

                if not flag:
                    ans.append([itr, j])
                    func(itr+1)
                    ans.pop()

        func(0)
        hs2 = []
        for indexes in answer:
            hsi = []
            # print(index)
            for index in indexes:
                i, j = index
                hi = ""
                for h in range(n):
                    if j == h:
                        hi += 'Q'
                    else:
                        hi += '.'
                hsi.append(hi)
            hs2.append(hsi)
        
                  
        return hs2


