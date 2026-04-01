# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first,second = head,head
        counter=0
        prev=None
        while first and counter !=n:
            first=first.next
            counter+=1

        if not first:
            return head.next

        while first.next:
            first=first.next
            second=second.next
        
        if second and second.next:
            second.next = second.next.next
        elif second:
            second=None
        else:
            return None

        return head

        