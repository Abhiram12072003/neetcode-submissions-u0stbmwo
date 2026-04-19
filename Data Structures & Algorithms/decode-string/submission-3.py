class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        def helper():
            ans = ""
            k = 0
            while self.i < len(s):
                c = s[self.i]
                if c.isdigit():
                    k = k*10 + int(c)
                elif c == '[':
                    self.i += 1
                    ans += k*helper()
                    k = 0
                elif c == ']':
                    return ans
                else:
                    ans += c
                self.i += 1
            return ans
        return helper()                    