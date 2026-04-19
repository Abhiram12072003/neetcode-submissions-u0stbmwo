class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        hs = []
        count = {}
        xi = []

        for i in range(n):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
            
        def func():
            if len(xi) == n:
                # ans.add(tuple(xi))
                hs.append(xi[:])
                return

            for key in count:
                if count[key]>0:
                    xi.append(key)
                    count[key] -= 1
                    func()
                    count[key] += 1
                    xi.pop()
        func()

        # return list(ans)
        return hs
            