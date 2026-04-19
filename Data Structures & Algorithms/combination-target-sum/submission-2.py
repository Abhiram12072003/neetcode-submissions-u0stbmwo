class Solution:
    def func(self, nums, itr, xi, n, target, curr):
        if target == curr:
            if xi not in self.answer:
                self.answer.append(xi[:])
            return
           
        for i in range(itr,n):

            if nums[i] + curr > target:
                break
            
            xi.append(nums[i])
            self.func(nums, i, xi, n, target, curr+nums[i])
            xi.pop()
        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        self.answer = []
        self.func(nums, 0, [], len(nums), target, 0)
        return self.answer
