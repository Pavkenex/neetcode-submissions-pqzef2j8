# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #pronalazak sredine liste
        slow,fast = head,head

        while fast and fast.next:
            slow=slow.next
            fast= fast.next.next
        
        #slow sada pokazuje na sredinu liste, taj deo liste je sada potrebno reverse-ovati
        
        curr = slow.next
        slow.next=None
        prev = None
        #reversovanje
        while curr:
            next = curr.next
            curr.next = prev
            prev=curr
            curr=next
    
        #Naizmenican merge
        tmp=prev
        node=head
        while tmp:
            next = node.next
            tmpNext =tmp.next
            node.next=tmp
            node=next
            tmp.next=node
            tmp=tmpNext
        


        


            

        


        