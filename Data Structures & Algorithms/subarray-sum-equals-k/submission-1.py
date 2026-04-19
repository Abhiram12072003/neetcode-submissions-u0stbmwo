class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        s = 0
        ans = 0
        d[0] = 1
        for num in nums:
            # print(d)
            s += num
            if s-k in d:
                ans += d[s-k]
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        return ans