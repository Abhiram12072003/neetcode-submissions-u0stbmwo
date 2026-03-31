class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]
        nums = sorted(nums)

        def func(itr, xi):
            if itr == n:
                return
            
            for i in range(itr, n):
                if itr != i and nums[i] == nums[i-1]:
                    continue
                xi.append(nums[i])
                ans.append(xi[:])
                # print(itr, i, nums[i], nums[itr])
                func(i+1, xi)
                xi.pop()
            
        func(0, [])
        return ans