# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]):
        if not head:
            return None
        newHead = None
        newHead = head
        if head.next:
            newHead = self.reverse(head.next)
            head.next.next = head
            head.next = None
        return newHead
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for i in range(left-1):
            prev = prev.next
        sublist_head = prev.next
        sublist_tail = sublist_head
        for i in range(right-left):
            sublist_tail = sublist_tail.next
        nextPointer = sublist_tail.next
        sublist_tail.next = None
        node = self.reverse(sublist_head)
        prev.next = node
        sublist_head.next = nextPointer
        return dummy.next 