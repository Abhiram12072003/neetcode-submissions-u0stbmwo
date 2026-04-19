class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        n = len(s)
        j = 0
        res = 0
        for i in range(n):
            while s[i] in h:
                h.remove(s[j])
                j += 1
            h.add(s[i])
            res = max(res, i-j+1)
        return res 