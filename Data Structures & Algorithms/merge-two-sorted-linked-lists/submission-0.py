from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:Optional[ListNode], list2:Optional[ListNode])->Optional[ListNode]:
        # time complexity: O(n)
        # space complexity:O(1)
        
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
        
    def printList(self,head):
        res = []
        cur = head
        
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
            
# list1 = [1,2,4], list2 = [1,3,5]  
list1 = ListNode(1,ListNode(2,ListNode(4,None)))
list2 = ListNode(1,ListNode(3,ListNode(5,None)))

head = Solution().mergeTwoLists(list1,list2)
print(Solution().printList(head))
            