class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for b in range(32):
            x = 1<<b
            cnt1, cnt2 = 0, 0
            for num in nums:
                if x & num:
                    cnt1 += 1
            for num in range(1, n):
                if num & x:
                    cnt2 += 1
            if cnt1 > cnt2:
                ans |= x
        return ans