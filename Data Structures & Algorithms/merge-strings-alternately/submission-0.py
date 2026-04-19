class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n1, n2 = len(word1), len(word2)
        i,j = 0, 0
        inc = 0
        while i<n1 and j<n2:
            if inc%2 ==0:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
            inc += 1
        
        while i<n1:
            ans += word1[i]
            i += 1
        while j<n2:
            ans += word2[j]
            j += 1
        return ans