# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node, k, prev):
        px = prev
        prev = None
        curr, tmp = node, node
        while k>0:
            if curr:
                tmp = curr.next
                curr.next = prev
            prev = curr
            curr = tmp
            k -= 1
        if not px:
            node.next = curr
            return node, prev

        px.next.next = curr
        px.next = prev
        return node, prev
    def print(self, node):
        while node:
            print(node.val, end = ' ')
            node = node.next
        print()

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        n = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            n += 1
        x = n//k
        pt = head
        cx = None
        prev = None
        while x>0:
            prev, nx = self.reverse(pt, k, prev)
            # print(prev.val)
            # self.print(prev)
            if x == n//k:
                cx = nx
            if prev:
                pt = prev.next
            # break
            x -= 1
        return cx