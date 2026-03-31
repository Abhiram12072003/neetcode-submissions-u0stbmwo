class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        ans = []

        def func(itr, xi, s):
            if s == target:
                ans.append(xi[:])
                return

            for i in range(itr, len(nums)):
                if i != itr and nums[i] == nums[i-1]:
                    continue

                if s + nums[i] > target:
                    break

                xi.append(nums[i])
                func(i+1, xi, s+nums[i])
                xi.pop()

        func(0, [], 0)
        return ans