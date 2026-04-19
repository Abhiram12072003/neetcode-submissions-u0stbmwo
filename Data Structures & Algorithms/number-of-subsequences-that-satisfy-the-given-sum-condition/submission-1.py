class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        i = 0
        ans = 0
        mod = 10**9 + 7
        j = n - 1
        while i<n:
            while i<=j and nums[i] + nums[j] > target:
                j -= 1
            if i<=j:
                ans += pow(2, j - i, mod)
                ans %= mod;
            i += 1
        return ans