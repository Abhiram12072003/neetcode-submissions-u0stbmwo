class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        d = {}
        for i in t:
            d[i] = 1 + d.get(i,0)
        need = len(d)
        res, reslen = [-1,-1], float("infinity")
        d2 = {}
        i,j = 0, 0
        have = 0
        while i < n:
            d2[s[i]] = 1 + d2.get(s[i],0)
            if d2[s[i]] == d.get(s[i],0) and d.get(s[i],0)!=0:
                have += 1
            while j<=i and have == need:
                d2[s[j]] -= 1
                if i-j+1<reslen:
                    reslen = i-j+1
                    res = [j,i]
                if d2[s[j]] < d.get(s[j], 0):
                    have -= 1
                j += 1
            i += 1
                    
        return s[res[0]: res[1]+1] if reslen != float("infinity") else ""