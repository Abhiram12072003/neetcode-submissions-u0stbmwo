class Solution:
    def func(self, nums, itr, xi, n):
        if itr == n:
            if xi[:] not in self.answer:
                self.answer.append(xi[:])
            return
        xi.append(nums[itr])
        self.func(nums, itr+1, xi, n)
        xi.pop()
        self.func(nums, itr+1, xi, n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # lis = list(set(nums))
        self.answer = []
        nums =sorted(nums)
        self.func(nums, 0, [], len(nums))
        return self.answer