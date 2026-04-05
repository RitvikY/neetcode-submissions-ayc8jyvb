# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        curr1 = list1
        curr2 = list2

        dummy = ListNode()
        prev = dummy


        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp = curr1.next
                prev.next = curr1  # Attach to the growing tail
                prev = prev.next   # Move the tail forward!
                curr1 = temp
            else:
                temp = curr2.next
                prev.next = curr2  # Attach to the growing tail
                prev = prev.next   # Move the tail forward!
                curr2 = temp
        if curr1:
            prev.next = curr1
        elif curr2:
            prev.next = curr2

        return dummy.next

        