class Solution:
    def func(self, val, xi, n, k):
        if len(xi) == k:
            self.answer.append(xi[:])
            return
        
        if val > n:
            return

        xi.append(val)
        self.func(val+1, xi, n, k)
        xi.pop()
        self.func(val+1, xi, n, k)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.answer = []
        self.func(1, [], n, k)
        return self.answer