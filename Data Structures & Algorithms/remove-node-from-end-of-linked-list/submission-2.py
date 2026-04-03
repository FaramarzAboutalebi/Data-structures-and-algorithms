from typing import Optional

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[NodeList], n: int)->Optional[NodeList]:
        # time complexity: O(n)
        # space complexity: O(1)
        if not head:
            return None

        dummy = NodeList(0,head)
        slow, fast = dummy,dummy
        
        while n:
            fast = fast.next
            n-=1
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next
    def printList(self, head: Optional[NodeList])->None:
        
        cur = head
        res = []
        
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)
            

# head = [1,2,3,4], n = 2
sol = Solution()
head = NodeList(1,NodeList(2,NodeList(3,NodeList(4))))
n = 2
head = sol.removeNthFromEnd(head, n)
sol.printList(head)
