# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def findMid(head):
            ptr1, ptr2 = head, head
            while ptr2 and ptr2.next:
                ptr1 = ptr1.next
                ptr2 = ptr2.next.next
            return ptr1
        def reverse(p2):
            # print(p2.val)
            ptr1, ptr2, ptr3 = None, p2, p2
            while ptr2:
                ptr3 = ptr2.next
                ptr2.next = ptr1
                ptr1 = ptr2
                ptr2 = ptr3
            # if ptr1:
            #     ptr2.next = ptr1
            # print(ptr2.val)
            return ptr1
        p1 = findMid(head)
        p2 = p1.next
        p1.next = None
        # print(p1.val,p2.val)
        p2 = reverse(p2)
        i = p2
        # while i:
        #     print(i.val, end = ' ')
        #     i = i.next
        # print()
        # print(p2.val)
        px1, px2 = head, p2
        ans = None
        h1 = None
        cnt = 0
        while px1 and px2:
            if cnt % 2 == 0:
                if not ans:
                    ans = px1
                    h1 = ans
                else:
                    ans.next = px1
                    ans = ans.next
                px1 = px1.next
            else:
                ans.next = px2
                ans = ans.next
                px2 = px2.next
            print(ans.val)
            ans.next = None
            cnt += 1
        if not ans:
            return None
        if px1:
            ans.next = px1
        if px2:
            ans.next = px2
        # return None