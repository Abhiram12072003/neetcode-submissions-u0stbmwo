class MyStack:
    q1 = None
    def __init__(self):
      self.q1 = deque() 

    def push(self, x: int) -> None:
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())

    def pop(self) -> int:
        return self.q1.popleft()
    def top(self) -> int:
        return self.q1[0]
    def empty(self) -> bool:
        return True if len(self.q1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()