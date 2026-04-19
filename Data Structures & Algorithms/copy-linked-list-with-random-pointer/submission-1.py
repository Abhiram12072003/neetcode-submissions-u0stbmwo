"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        ptr = dummy
        d = {}
        cnt = 0
        px = head
        while head:
            dummy.next = Node(head.val)
            dummy = dummy.next
            # cnt += 1
            d[head] = dummy
            head = head.next
        ptr2 = ptr.next
        while px:
            # print(px.val)
            if px.random:
                ptr2.random = d[px.random]
                # print(px.random)
                # ptr2.random = d[px].random           
            px = px.next
            ptr2 = ptr2.next
        return ptr.next
            