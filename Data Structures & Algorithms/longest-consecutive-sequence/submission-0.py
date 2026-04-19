class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        ans = 0
        for num in s:
            if num-1 not in s:
                x = num + 1
                cnt = 1
                while x in s:
                    x += 1
                    cnt += 1
                ans = max(ans, cnt)
        return ans