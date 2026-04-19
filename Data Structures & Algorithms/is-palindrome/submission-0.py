class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        y = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                x = i + x
                y += i
        return x == y