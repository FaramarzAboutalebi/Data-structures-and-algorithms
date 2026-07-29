from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time complexity: O(n log k)
        # space complexity: O(k)
        while len(lists) > 1:
            level = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                level.append(self.mergeTwoList(list1, list2))
            lists = level
                
        return lists[0] if lists else None
    def mergeTwoList(self, l1: Optional[ListNode], l2: Optional[ListNode])->Optional[ListNode]:
        # time complexity: O(n)
        # space complexity: O(1)
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next  
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next
        

