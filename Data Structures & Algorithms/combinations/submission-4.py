class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        xi = []
        ans = []
        def func(itr, xi):
            if len(xi) == k:
                ans.append(xi[:])
                return
            for i in range(itr, n+1):
                if (k - len(xi)) > n-itr+1:
                    break 
                xi.append(i)
                func(i+1, xi)
                xi.pop()
            return
        func(1,xi)
        return ans