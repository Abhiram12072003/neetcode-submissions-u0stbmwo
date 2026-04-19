class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for mask in range(1<<len(nums)):
            xi = []
            for i in range(len(nums)):
                # print(mask)
                if mask & (1<<i):
                    xi.append(nums[i])
            ans.append(xi)
        return ans