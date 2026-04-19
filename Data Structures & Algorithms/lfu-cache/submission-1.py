class ListNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0, self.left)
        self.left.next = self.right
        self.mp = {}
    def len(self):
        return len(self.mp)
    def pushright(self, k, v):
        node = ListNode(k, v, self.right.prev, self.right)
        self.mp[k] = node
        self.right.prev = node
        node.prev.next = node
    def pop(self, k):
        if k in self.mp:
            node = self.mp[k]
            previ, nexti = node.prev, node.next
            node.prev, node.next = None, None
            previ.next, nexti.prev = nexti, previ
            self.mp.pop(k, None)
    def popLeft(self):
        res = self.left.next.key
        self.pop(self.left.next.key)
        return res
    def retreive(self):
        ptr = self.left.next
        while ptr != self.right:
            print('{', ptr.key, ':', ptr.val, '}', end = ':')
            ptr = ptr.next
        print()

class LFUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        self.cap = capacity
        self.cntList = defaultdict(LinkedList)
        self.lfucnt = 0
        self.cntDict = defaultdict(int)

    def counter(self, key):
        cnt = self.cntDict[key]
        self.cntDict[key] += 1
        self.cntList[cnt].pop(key)
        self.cntList[cnt+1].pushright(key, self.kv[key])
        if cnt == self.lfucnt and self.cntList[cnt].len() == 0:
            self.lfucnt += 1
        
    def get(self, key: int) -> int:
        print("find:", key)
        print(self.kv)
        print("cntDict:",self.cntDict)
        if key not in self.kv:
            return -1
        self.counter(key)
        for k in self.cntList:
            if k == 0:
                continue
            print("K:", k)
            x = self.cntList[k]
            x.retreive()
        print("cntDict:",self.cntDict)
        print("lfucnt:",self.lfucnt)
        print("kv:", self.kv)
        return self.kv[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.kv and len(self.kv) == self.cap:
            res = self.cntList[self.lfucnt].popLeft()
            self.kv.pop(res, None)
            self.cntDict.pop(res, None)
            print("Res:",res)
        self.kv[key] = value
        print("Put: cntDict:", self.cntDict)
        self.counter(key)
        self.lfucnt = min(self.lfucnt, self.cntDict[key])
        print("fff:", self.lfucnt, key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)