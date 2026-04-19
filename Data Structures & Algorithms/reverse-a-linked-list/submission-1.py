# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]):
        if not head:
            return None
        new_head = head
        if head.next:
            new_head = self.reverse(head.next)
            head.next.next = head
            head.next = None
        return new_head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)