class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def func(itr):
            if itr == len(nums):
                ans.append(nums[:])
                return

            for i in range(itr, n):
                nums[itr], nums[i] = nums[i], nums[itr]
                func(itr+1)
                nums[itr], nums[i] = nums[i], nums[itr]
            return
    
        func(0)
        
        return ans