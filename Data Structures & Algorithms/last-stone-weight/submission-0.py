class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-i for i in stones]
        heapq.heapify(st)
        while len(st)>=2:
            x, y = heapq.heappop(st), heapq.heappop(st)
            if x != y:
                heapq.heappush(st, -abs(x-y))
        if st:
            return -st[0]
        return 0        