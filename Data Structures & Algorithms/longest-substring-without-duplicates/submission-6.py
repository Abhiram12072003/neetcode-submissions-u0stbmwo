class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        d = {}
        i,j = 0,0
        while i<n:
            if s[i] in d and d[s[i]]>=j:
                j = d[s[i]]
                j += 1
            d[s[i]] = i
            ans = max(ans, i-j+1)
            # print(i,j, d)
            i += 1

        return ans