class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []
        def func(itr, xi):
            if itr == len(s):
                ans.append(xi)
                return

            hi = ""
            
            for i in range(itr, n):
                hi += s[i]
                if hi in wordDict:
                    if xi != "":
                        hp = xi + " " + hi
                    else:
                        hp = hi
                    func(i+1, hp)
        func(0, "")
        return ans