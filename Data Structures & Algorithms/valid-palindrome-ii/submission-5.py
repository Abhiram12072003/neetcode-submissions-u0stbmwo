class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        cnt = 0
        n = len(s)
        while i<=j:
            if s[i] != s[j]:
                # Try skipping left character OR skipping right character
                case1 = s[i+1:j+1]
                case2 = s[i:j]
                print(case1, case2)
                return case1 == case1[::-1] or case2 == case2[::-1]
            i += 1
            j -= 1
        return True