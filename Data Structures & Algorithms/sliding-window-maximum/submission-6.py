class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i = 0
        mx = 0
        ans = []
        q = deque()
        while i<n:
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            if q and q[0]<=i-k:
                q.popleft()
            q.append(i)
            # print(q)
            if i>=k-1:
                ans.append(nums[q[0]])
            i += 1 
        return ans
