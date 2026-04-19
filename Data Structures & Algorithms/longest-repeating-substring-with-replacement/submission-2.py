class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i,j = 0,0
        d = {}
        mx = 0
        ans = 0
        while j<n:
            d[s[j]] = 1 + d.get(s[j],0)
            if mx<d[s[j]]:
                mx = d[s[j]]
            while i<=j and (j-i+1) - mx > k:
                d[s[i]] -= 1
                i += 1
            if (j-i+1) - mx <= k:
                ans = max(ans, j-i+1) 
            j += 1
        return ans