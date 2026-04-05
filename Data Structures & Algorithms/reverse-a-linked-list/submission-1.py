# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None


        # 0 1 2 3 4 

        while curr:
            tmp = curr.next # 1
            curr.next = prev # 0
            prev = curr
            curr = tmp 

        return prev