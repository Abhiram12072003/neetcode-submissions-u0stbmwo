class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        lis = []
        ans = []

        for idx, t in enumerate(tasks):
            t.append(idx)
        
        tasks.sort()
        
        heapq.heappush(lis, [tasks[0][1],tasks[0][2]])
        t, itr = tasks[0][0], 1

        while itr < len(tasks) or lis:
            fg = False
            if lis:
                ele = heapq.heappop(lis)
                fg = True
                ans.append(ele[-1])
                t += ele[0]

            while itr<len(tasks) and t >= tasks[itr][0]:
                heapq.heappush(lis, [tasks[itr][1], tasks[itr][2]])
                itr += 1
            if not fg and itr < len(tasks):
                t = tasks[itr][0]
            # print(t, lis)
        
        return ans