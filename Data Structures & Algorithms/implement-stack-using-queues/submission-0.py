class MyStack:
    q1 = None
    def __init__(self):
      self.q1 = deque()  

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        q2 = deque()
        top = 0
        while not self.empty():
            x = self.q1.popleft()
            if self.empty():
                top = x
                break
            q2.append(x)
        self.q1 = q2
        return top
    def top(self) -> int:
        q2 = deque()
        top = 0
        print("top",self.empty())
        while not self.empty():
            x = self.q1.popleft()
            if self.empty():
                top = x
            q2.append(x)
        self.q1 = q2
        return top
    def empty(self) -> bool:
        return True if len(self.q1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()