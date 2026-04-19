class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans = 0
        ls = [[l1, l2] for l1,l2 in zip(capital, profits)]
        ls = sorted(ls)
        n = len(ls)
        i = 0
        lis = []
        cnt = 0
        print(ls)
        while i<n or lis:
            fg = False
            while i < n and ls[i][0]<=w:
                print(ls[i])
                heapq.heappush(lis, [-ls[i][1]])
                fg = True
                i += 1
            xi = True
            print(i)
            if lis and cnt < k and not fg:
                xi = False
                ptr = (heapq.heappop(lis))
                print(ptr)
                # ans += abs(ptr[0])
                w += abs(ptr[0])
                print("w", w)
                cnt += 1
            if xi and not fg:
                break
        return w
        # while True:
            