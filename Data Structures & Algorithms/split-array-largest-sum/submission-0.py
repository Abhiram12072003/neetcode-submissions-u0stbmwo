class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def func(nums, m, k):
            ans = 0
            s = 0
            cnt = 1
            for i in nums:
                s += i
                if s > m:
                    s = i
                    cnt += 1
            return cnt
        n = len(nums)
        s = 0
        for i in nums:
            s += i
        l,h = max(nums), s
        while l<=h:
            m = (l+h)//2
            sh = func(nums,m,k)
            if sh>k:
                l = m + 1
            else:
                h = m - 1
        return l