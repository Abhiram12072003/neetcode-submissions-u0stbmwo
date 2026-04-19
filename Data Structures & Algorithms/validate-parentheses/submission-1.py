class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        n = len(s)
        d = {'(':')', '{':'}', '[':']'}
        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                q.append(s[i])
            else:
                if q and d[q[-1]] == s[i]:
                    q.pop()
                else:
                    return False
        return True if len(q) == 0 else False