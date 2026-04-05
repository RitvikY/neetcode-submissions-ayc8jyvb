# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode()
        prev = res

        curr1 = l1
        curr2 = l2
        carry = 0


        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0.
            val2 = curr2.val if curr2 else 0.
            sum = int(val1 + val2) + carry
            print(sum)

            if sum < 10:
                carry = 0
            elif sum >= 10:
                sum -= 10
                carry = 1

        
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            sumNode = ListNode(sum)
            res.next = sumNode
            res = res.next


        
        if carry > 0:
            res.next = ListNode(carry)
            res = res.next

        return prev.next
        


        