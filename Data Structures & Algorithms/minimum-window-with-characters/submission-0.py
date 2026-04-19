class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        d = {}
        for i in t:
            d[i] = 1 + d.get(i,0)
        res, reslen = [-1,-1], float("infinity")
        for i in range(n):
            d2 = {}
            for j in range(i,n):
                d2[s[j]] = 1 + d2.get(s[j],0)
                flag = True
                for ch in d:
                    if d[ch] > d2.get(ch,0):
                        flag = False
                        break
                if flag and j-i+1<reslen:
                    reslen = j-i+1
                    res = [i,j]
                    
        return s[res[0]: res[1]+1] if reslen != float("infinity") else ""