# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1, ptr2 = head, head
        itr = 0
        while itr<n:
            ptr2 = ptr2.next
            itr += 1
        pt = None
        while ptr2:
            # print(1)
            ptr2 = ptr2.next
            pt = ptr1
            ptr1 = ptr1.next
        if ptr1:
            if pt:
                pt.next = ptr1.next
            else:
                head = head.next
            ptr1.next = None
            return head
        return None