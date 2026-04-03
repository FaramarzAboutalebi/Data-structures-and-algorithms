from typing import Optional

class LinkNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[LinkNode], n:int)->Optional[LinkNode]:
        
        if not head:
            return None
        
        dummy = LinkNode(0, head)
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
# space complexity:  O(1)     
n = 2
head = LinkNode(1, LinkNode(2, LinkNode(3, LinkNode(4, None))))
res = Solution().removeNthFromEnd(head,n)
print(res)

cur = res
while cur:
    print(cur.val, end="->")
    cur = cur.next

