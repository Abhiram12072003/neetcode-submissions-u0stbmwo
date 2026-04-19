class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            while j <= n-3:
                k = j + 1
                k2 = n-1
                s = nums[i] + nums[j]
                while k < k2:
                    if s + nums[k] + nums[k2] == target:
                        res.append([nums[i], nums[j], nums[k], nums[k2]])
                        k += 1
                        k2 -= 1
                        while k < k2 and nums[k] == nums[k-1]:
                            k += 1
                        while k < k2 and nums[k2] == nums[k2+1]:
                            k2 -= 1
                    elif s + nums[k] + nums[k2] < target:
                        k += 1
                    else:
                        k2 -= 1
                j += 1
                while j <= n-3 and nums[j] == nums[j-1]:
                    j += 1
        return res