class Solution:
    
    def checkPal(self, s):
        i, j = 0, len(s)-1
        while i<=j and s[i] == s[j]:
            i += 1
            j -= 1
        return True if i>j else False

    def func(self, s, itr, xi, st):
        if itr == len(s):
            self.answer.append(st[:])
            return
        for i in range(itr, len(s)):
            xi += s[i]
            if not self.checkPal(xi):
                continue
            st.append(xi)
            self.func(s, i+1, "", st)
            st.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        self.func(s, 0, "", [])
        return self.answer