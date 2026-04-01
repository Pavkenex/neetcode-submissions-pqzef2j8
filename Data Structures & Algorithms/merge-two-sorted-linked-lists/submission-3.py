# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        if not list1:
            return list2
        if not list2:
            return list1

        newList=None
        newListCurrent=None
        curr1,curr2=list1,list2
        
        if curr1.val<curr2.val:
            newList=curr1
            curr1=curr1.next
        else:
            newList=curr2
            curr2=curr2.next

        newListCurrent=newList
        while curr1 or curr2:
            
            if not curr1:
                newListCurrent.next=curr2
                break
            if not curr2:
                newListCurrent.next=curr1
                break
           
            if curr1.val<curr2.val:
                newListCurrent.next=curr1
                newListCurrent=newListCurrent.next
                curr1=curr1.next
                print("usao u prvu proveru")
            else:
                newListCurrent.next=curr2
                newListCurrent=newListCurrent.next
                curr2=curr2.next
                print("usao u drugu proveru")
            
        return newList
            
            
        


