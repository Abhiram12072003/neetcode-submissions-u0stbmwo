class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        n = len(s)
        ans = 0
        l = 0
        for i in range(n):
            if s[i] in d:
                l = max(d[s[i]] + 1,l)
            d[s[i]] = i
            ans = max(i-l+1,ans)
        return ans