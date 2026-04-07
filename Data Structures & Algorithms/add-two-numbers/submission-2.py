# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=head=ListNode()
        curr1 = l1
        curr2 = l2
        
        while curr1 and curr2:
            val = curr1.val+ curr2.val
            if val>=10:
                if curr1.next:
                    curr1.next.val+= 1
                else:
                    curr1.next = ListNode(1)
                val-=10
            dummy.next = ListNode(val)
            dummy=dummy.next
            curr1=curr1.next
            curr2=curr2.next

        if not curr1:
            dummy.next = curr2 if curr2 else None
        elif not curr2:
            temp=curr1
            while curr1:
                if curr1.val >= 10:
                    if curr1.next:
                        curr1.next.val+= 1
                        
                    else:
                        curr1.next = ListNode(1)
                    curr1.val-=10
                curr1=curr1.next
            dummy.next = temp
            
        
        return head.next
       
        