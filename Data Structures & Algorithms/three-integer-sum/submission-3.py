class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, j, k = 0, 0, 0
        n = len(nums)
        res = []
        for i, ele in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n - 1
            while j<k:
                if nums[j] + nums[k] + ele == 0:
                    res.append([ele, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    k-=1
                    j+=1
                elif ele + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res