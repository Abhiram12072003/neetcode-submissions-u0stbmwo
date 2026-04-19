class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lis = []
        ans = []
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            while lis and temperatures[lis[-1]]<=temperatures[i]:
                lis.pop()
            if not lis:
                ans.append(0)
            else:
                ans.append(lis[-1]-i)
            lis.append(i)   
            print([temperatures[j] for j in lis])
        return ans[::-1]