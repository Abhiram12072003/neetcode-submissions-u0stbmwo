class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        d = dict(Counter(tasks))
        print(d)
        for i in d:
            maxHeap.append(-d[i])
        heapq.heapify(maxHeap)
        q = deque()
        ans = 0
        print(maxHeap)
        while maxHeap or q:
            ans += 1
            if maxHeap:
                no = heapq.heappop(maxHeap)
                time = ans + n
                if no+1:
                    q.append([no+1,time])
            if q:
                no, t = q[0]
                if t == ans:
                    heapq.heappush(maxHeap, no)
                    q.popleft()
            # if ans == 10:
            #     break
            print(ans, maxHeap, q)
        return ans
