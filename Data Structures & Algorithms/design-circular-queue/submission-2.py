class ListNode:
    def __init__(self, val, nxt = None):
        self.val = val
        self.next = nxt
class MyCircularQueue:

    def __init__(self, k: int):
        self.rear = ListNode(0)
        self.front = self.rear
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear.next = ListNode(value)
        self.rear = self.rear.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        tmp = self.front.next
        self.front.next = self.front.next.next
        if not self.front.next:
            self.rear = self.front
        tmp.next = None
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()