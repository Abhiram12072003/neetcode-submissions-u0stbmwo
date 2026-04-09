class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)
        
        for x,y in edges:
            d[x].append(y)
            d[y].append(x)
        
        vis = set()
        visited = [False] * n

        def func(x, prev):
            if x in vis:
                return True
            if visited[x]:
                return False
            vis.add(x)
            visited[x] = True
            for chd in d[x]:
                if chd != prev:
                    if func(chd, x):
                        return True
            vis.remove(x)
            return False
        cnt = 0
        for i in range(n):
            if not visited[i]:
                if cnt != 0:
                    return False
                b = func(i, 101)  
                if b:
                    return False
                cnt += 1
        return True