class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        answer = []
        mapchartoidx = {}
        cnt = 0
        for x, y in equations:
            if x not in mapchartoidx:
                mapchartoidx[x] = cnt
                cnt += 1
            if y not in mapchartoidx:
                mapchartoidx[y] = cnt
                cnt += 1
        
        adj = [[] for i in range(cnt)]

        for i in range(len(equations)):
            x, y = equations[i]
            adj[mapchartoidx[x]].append((mapchartoidx[y], values[i]))
            adj[mapchartoidx[y]].append((mapchartoidx[x], 1/values[i]))
        print(adj)
        def dfs(src, prev, target, val, cnt):
            if src in vis:
                return
            nonlocal mnCnt, ans
            if target == src:
                # print(cnt, mnCnt)
                if mnCnt == -1:
                    mnCnt = cnt
                # print(mnCnt, cnt)
                if cnt <= mnCnt:
                    # print("1", val)
                    mnCnt = cnt
                    ans = val
                    # print(ans)
                return
            vis.add(src)
            # if src not in adj:
            #     print(src)
            #     return
            for chd in adj[src]:
                if chd[0] == prev:
                    continue
                dfs(chd[0], src, target, val*chd[1], cnt+1)
            vis.remove(src)
        
        for x, y in queries:
            vis, mnCnt, ans = set(), -1, -1
            if x not in mapchartoidx or y not in mapchartoidx:
                answer.append(-1)
                continue
            print((x,y))
            x, y = mapchartoidx[x], mapchartoidx[y]
            dfs(x, -1, y, 1, 0)
            answer.append(ans)
        
        return answer

