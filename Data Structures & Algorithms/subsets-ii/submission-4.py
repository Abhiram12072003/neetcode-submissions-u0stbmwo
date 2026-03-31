class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]
        xi = []
        nums = sorted(nums)

        def func(itr):
            if itr == n:
                return
            
            for i in range(itr, n):
                if itr != i and nums[i] == nums[i-1]:
                    continue
                xi.append(nums[i])
                ans.append(xi[:])
                # print(itr, i, nums[i], nums[itr])
                func(i+1)
                xi.pop()
            
        func(0)
        return ans