class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = [-i for i in nums]
        heapq.heapify(x)
        i = 1
        while i<k:
            heapq.heappop(x)
            i += 1
        return -x[0]