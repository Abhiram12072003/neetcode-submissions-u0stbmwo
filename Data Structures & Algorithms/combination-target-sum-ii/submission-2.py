class Solution:
    def func(self, nums, itr, xi, ans, target):
        if ans == target:
            # print(xi)
            if xi not in self.answer:
                self.answer.append(xi[:])
            return
        if itr == len(nums):
            return
        
        for i in range(itr, len(nums)):
            # print('xi:', xi)
            if i > itr and nums[i] == nums[i-1]:
                continue
            if ans + nums[i] > target:
                break
            xi.append(nums[i])
            self.func(nums, i+1, xi, ans+nums[i], target)
            xi.pop()
        
        return
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates):
            return []
        candidates = sorted(candidates)
        self.answer = []
        print(candidates)
        # self.func(candidates, 0, [candidates[0]], candidates[0], target)
        self.func(candidates, 0, [], 0, target)
        # self.answer = list(self.answer)
        return self.answer
        