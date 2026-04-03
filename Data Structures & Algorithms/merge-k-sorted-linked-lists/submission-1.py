from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]])->Optional[ListNode]:
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedL = self.mergeTwoList(l1,l2)
                mergedList.append(mergedL)
            
            lists = mergedList 
        return lists[0] if len(lists) > 0 else None
        
    def mergeTwoList(self, list1:Optional[ListNode],list2:Optional[ListNode])->Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
                
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return dummy.next
    def printList(self, head):
        res = []
        cur = head
        
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
lists = [ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(5))),ListNode(3,ListNode(6))]
head = Solution().mergeKLists(lists)
print(Solution().printList(head) == [1,1,2,3,3,4,5,6])



        