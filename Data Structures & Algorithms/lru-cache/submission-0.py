class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.left = ListNode(1,1)
        self.right = ListNode(1,1)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node: ListNode):
        previ = node.prev
        nexti = node.next
        node.prev, node.next = None, None
        previ.next, nexti.prev = nexti, previ
    
    def insert(self, node: ListNode):
        prevR = self.right.prev
        prevR.next, self.right.prev = node, node
        node.next, node.prev = self.right, prevR

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        #remove
        self.remove(node)
        #insert
        self.insert(node)
        self.d[key] = node
        return self.d[key].val

    def put(self, key: int, value: int) -> None:
        #insert
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.remove(node)
        elif len(self.d) == self.cap:
            k = self.left.next.key
            del self.d[k]
            #remove
            # print(key, val)
            self.remove(self.left.next)
            self.d[key] = ListNode(key, value)
            node = self.d[key]
        else:
            self.d[key] = ListNode(key, value)
            node = self.d[key]
        self.insert(node)
