from typing import Optional

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int)->Optional[ListNode]:
        
        dummy = ListNode(0,head)
        
        fast,slow = dummy,dummy
        
        while n:
            fast = fast.next
            n -= 1
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
# time complexity: O(n)
# space complexity: O(1)   
# 1->2->3->4
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))
n = 2
res = Solution().removeNthFromEnd(head,n)
cur = res
while cur:
    print(cur.val, end= " -> ")
    cur = cur.next
print("None")