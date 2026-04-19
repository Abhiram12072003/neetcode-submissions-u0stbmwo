import bisect
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []
        
        wordDict = sorted(wordDict)
        
        def find(word):
            idx = bisect.bisect_left(wordDict,word)
            if idx < len(wordDict) and wordDict[idx] == word:
                return True
            return False

        def func(itr, xi):
            if itr == len(s):
                ans.append(xi)
                return

            hi = ""
            
            for i in range(itr, n):
                hi += s[i]
                if find(hi):
                    if xi != "":
                        hp = xi + " " + hi
                    else:
                        hp = hi
                    func(i+1, hp)
        func(0, "")
        return ans