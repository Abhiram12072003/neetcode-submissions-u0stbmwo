class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)
        dp = [0]*n
        def func(itr):
            if itr == n:
                return 0
            
            xi = ""
            
            if dp[itr] != 0:
                return dp[itr]

            val = 1 + func(itr+1)

            for i in range(itr, n):
                xi += s[i]
                if xi in dictionary:
                    val = min(val, func(i+1))
            
            dp[itr] = val
            return val
        
        return func(0)
        