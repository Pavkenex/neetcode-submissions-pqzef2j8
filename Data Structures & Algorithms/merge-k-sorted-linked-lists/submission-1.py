# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                mergedList.append(self.mergeList(l1,l2))
            lists = mergedList
        return lists[0]

    
    def mergeList(self,list1, list2) ->Optional[ListNode]:
        dummy = node = ListNode()
        curr1,curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val<curr2.val:
                node.next=curr1
                curr1=curr1.next
            else:
                node.next=curr2
                curr2 = curr2.next
            node=node.next
        
        node.next = curr1 or curr2
        return dummy.next
        