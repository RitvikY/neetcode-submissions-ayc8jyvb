# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        #get length
        while curr:
            size+=1
            curr = curr.next

        node_to_remove = (size - n) 
        if node_to_remove == 0 :
            return head.next

        switch, prev = head, head

        for i in range(node_to_remove-1):
            switch = switch.next
            print(switch.val)
        switch.next = switch.next.next
        return prev
            
        
            