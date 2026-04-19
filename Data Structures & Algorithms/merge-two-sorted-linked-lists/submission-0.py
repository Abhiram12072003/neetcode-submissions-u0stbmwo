# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lis = None
        h1 = None
        while list1 and list2:
            if list1.val <= list2.val:
                if not lis:
                    lis = list1
                    h1 = lis
                else:
                    lis.next = list1
                    lis = lis.next
                list1 = list1.next
            else:
                if not lis:
                    lis = list2
                    h1 = lis
                else:
                    lis.next = list2
                    lis = lis.next
                list2 = list2.next
            lis.next = None
        if list1:
            if lis:
                lis.next = list1
            else:
                lis = list1
                h1 = lis
        if list2:
            if lis:
                lis.next = list2
            else:
                lis = list2
                h1 = lis
        return h1