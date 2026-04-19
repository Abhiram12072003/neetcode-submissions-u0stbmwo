class Solution:
    def func(self, nums, itr, ans, target, xi):
        if itr == len(nums):
            return
        if ans == target:
            if xi:
                self.answer.append(xi[:])
                xi = []
            return
        
        for i in range(itr, len(nums)):
            if ans+nums[i] > target:
                break
            xi.append(nums[i])
            self.func(nums, i, ans+nums[i], target, xi)
            xi.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target < min(nums):
            return []
        n = len(nums)
        nums = sorted(nums)
        self.answer = []
        self.func(nums, 0, 0, target, [])
        return self.answer