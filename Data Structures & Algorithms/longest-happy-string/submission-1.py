class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a' :  a, 'b' :  b, 'c' : c}
        lis = [[-d[k], k] for k in d if d[k] != 0]
        ans = ""
        
        heapq.heapify(lis)
        
        prev = None
        while lis:
            cnt, char = heapq.heappop(lis)
            if len(ans)>1 and ans[-2] == ans[-1] == char:
                if not lis:
                    break
                cnt2, char2 = heapq.heappop(lis)
                ans += char2
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(lis, [cnt2, char2])
            else:
                ans += char
                cnt += 1
            if cnt != 0:
                heapq.heappush(lis, [cnt, char])
        return ans