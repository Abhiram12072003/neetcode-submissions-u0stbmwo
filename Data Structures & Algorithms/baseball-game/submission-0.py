class Solution:
    def calPoints(self, operations: List[str]) -> int:
        dq = deque()
        for i in operations:
            if i not in ("+", "C", "D"):
                dq.append(int(i))
            elif i == "+":
                dq.append((dq[-1])+(dq[-2]))
            elif i == "C":
                dq.pop()
            else:
                dq.append((dq[-1])*2)
            print(dq)
        ans = 0
        while dq:
            ans += int(dq.pop())
        return ans
            
