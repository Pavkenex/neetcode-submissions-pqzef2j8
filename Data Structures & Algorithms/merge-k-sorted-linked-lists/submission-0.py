# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while True:
            # izbaci prazne liste
            lists = [lst for lst in lists if lst]

            # ako vise nema nijedne liste, gotovo
            if not lists:
                break

            minVal = float("inf")
            index = -1

            # prodji kroz SVE liste
            for i in range(len(lists)):
                if lists[i].val < minVal:
                    minVal = lists[i].val
                    index = i

            # zakaci najmanji cvor
            node.next = lists[index]
            node = node.next

            # pomeri tu listu na sledeci cvor
            lists[index] = lists[index].next

        return dummy.next