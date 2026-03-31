class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        def func(itr, s, xi):
            if s == target:
                ans.append(xi[:])
            for i in range(itr,len(nums)):
                if s + nums[i]>target:
                    break
                xi.append(nums[i])
                func(i,s+nums[i],xi)
                xi.pop()
        func(0, 0, [])
        return ans