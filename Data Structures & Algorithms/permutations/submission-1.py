class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def func(itr, xi, nums):
            if itr == len(nums):
                ans.append(xi[:])
                return

            for i in range(itr, n):
                nums[itr], nums[i] = nums[i], nums[itr]
                xi.append(nums[itr])
                func(itr+1, xi, nums)
                xi.pop()
                nums[itr], nums[i] = nums[i], nums[itr]
            return
    
        func(0,[], nums)
        
        return ans