from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode])->Optional[ListNode]:
        # time complexity: O(n)
        # space complexity:O(1)
        if not head: 
            return None
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
    def printList(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
# head = [0,1,2,3]
head = ListNode(0,ListNode(1,ListNode(2,ListNode(3,None))))
head = Solution().reverseList(head)

print(Solution().printList(head))

        
