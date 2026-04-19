class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        lis = []
        
        for i in range(len(tasks)):
            ele = tasks[i]
            heapq.heappush(lis,[ele[0], ele[1], i])

        ans = []
        ls = []
        t = 0
        while lis or ls:
            fg = False
            
            while lis and t >= lis[0][0]:
                x = heapq.heappop(lis)
                heapq.heappush(ls, [x[1], x[2]])
            
            if not ls:
                t = lis[0][0]
                continue
            
            x = heapq.heappop(ls)
            ans.append(x[-1])
            t += x[0]

        return ans