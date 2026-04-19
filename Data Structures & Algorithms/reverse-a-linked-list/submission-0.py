# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next == None:
            return head
        ptr1, ptr2 = None, head
        ptr3 = head
        while ptr2 and ptr2.next != None:
            ptr3 = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
        if ptr2:
            ptr2.next = ptr1
        return ptr2
