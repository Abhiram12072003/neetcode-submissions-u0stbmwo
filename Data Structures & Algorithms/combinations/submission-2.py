class Solution:
    def func(self, val, xi, n, k):
        if len(xi) == k:
            self.answer.append(xi[:])
            xi = []
            return
        if val>n:
            return
        for i in range(val, n+1):
            if len(xi) > k:
                break
            xi.append(i)
            self.func(i+1,xi,n,k)
            xi.pop()
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.answer = []
        self.func(1, [], n, k)
        return self.answer