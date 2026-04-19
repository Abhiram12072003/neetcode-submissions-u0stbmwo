class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        n = len(s)
        i, j = 0, 0
        maxf = 0
        ans = 0
        while j<n:
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            maxf = max(maxf, d[s[j]])
            while (j-i+1)-maxf > k:
                d[s[i]] -= 1
                i += 1
                maxf = max(d.values())
            ans = max(ans, j-i+1)
            j += 1

        return ans