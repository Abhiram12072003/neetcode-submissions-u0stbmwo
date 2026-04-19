# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode], n):
        if n == 1:
            return head, head.next
        node_head, next_node = self.reverse(head.next, n-1)
        head.next.next = head
        head.next = next_node
        return node_head, next_node
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            node, _ = self.reverse(head, right)
            return node
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head