from typing import Optional

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
class Solution:
    def reorderList(self, head: Optional[NodeList])->None:
        # time complexity: O(n)
        # space complexity: O(1)
        if not head:
            return None
        
        slow,fast = head,head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        l2 = slow.next
        slow.next = None
        l2 = self.reverse(l2)
        l1 = head
        while l2:
            temp1,temp2 = l1.next,l2.next
            l1.next = l2
            l2.next = temp1
            l1,l2 = temp1,temp2
        
    def reverse(self, head: Optional[NodeList])->Optional[NodeList]:
        
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    def printList(self, head: Optional[NodeList])->None:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)
        
   
      

head = NodeList(2,NodeList(4,NodeList(6,NodeList(8))))
Solution().reorderList(head) 
Solution().printList(head)