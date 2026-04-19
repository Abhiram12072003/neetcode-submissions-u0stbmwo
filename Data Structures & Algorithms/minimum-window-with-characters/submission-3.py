class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        i, j = 0, 0
        d1 = {}
        for ch in t:
            d1[ch] = d1.get(ch,0) + 1
        pt = len(d1)
        d2 = {}
        p1, ans = 0, float("infinity")
        xi = []
        while i<n:
            d2[s[i]] = d2.get(s[i], 0) + 1
            if s[i] in d1 and d1[s[i]] == d2[s[i]]:
                p1 += 1
            while j<=i and p1 == pt:
                if ans>i-j+1:
                    ans = i-j+1
                    xi = [j,i]            
                d2[s[j]] -= 1
                if s[j] in d1 and d1[s[j]] > d2[s[j]]:
                    p1 -= 1
                j += 1
            i += 1
        # print(ans)
        return s[xi[0]:xi[1]+1] if len(xi)==2 else ""