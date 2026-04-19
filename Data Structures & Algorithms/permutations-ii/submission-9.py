class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums = sorted(nums)
        def func(xi):
            if len(xi) == n:
                ans.add(tuple(xi))
                return
            for i in range(n):
                if nums[i] != float("-inf"):
                    xi.append(nums[i])
                    nums[i] = float("-inf")
                    func(xi)
                    nums[i] = xi[-1]
                    xi.pop()
        func([])

        return list(ans)
            