# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # time complexity: O(n)
        # space complexity: O(1)

        slow, fast = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l2 = slow.next
        slow.next = None
        l2 = self.reverse(l2)
        l1 = head

        while l2:
            t1,t2 = l1.next,l2.next
            l1.next = l2
            l2.next = t1
            l1,l2 = t1,t2
        

    def reverse(self, head: Optional[ListNode])->Optional[ListNode]:

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

        
        