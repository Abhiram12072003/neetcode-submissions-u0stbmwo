class Solution:
    
    def checkPal(self, s):
        i, j = 0, len(s)-1
        while i<=j and s[i] == s[j]:
            i += 1
            j -= 1
        return True if i>j else False
        
    def func(self, s, xi, itr):
        if itr == len(s):
            self.answer.append(xi[:])
        
        sc = ""
        
        for i in range(itr, len(s)):
            sc += s[i]
            if self.checkPal(sc):
                xi.append(sc)
                self.func(s, xi, i+1)
                xi.pop()
        

    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        self.func(s, [], 0)
        return self.answer