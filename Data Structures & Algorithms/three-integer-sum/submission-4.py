class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        print(nums)
        i = 0
        while i<n-2:
            x = nums[i]
            j, k = i+1, n-1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i<n-2 and nums[i] == nums[i-1]:
                i += 1
        return res