class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        i, j = 0, n-1
        mod = 1000000007
        ans = 0
        while i<=j:
            if nums[i] + nums[j] <= target:
                ans += pow(2, j-i, mod)
                ans = ans%mod
                i += 1
            else:
                j -= 1
        return ans