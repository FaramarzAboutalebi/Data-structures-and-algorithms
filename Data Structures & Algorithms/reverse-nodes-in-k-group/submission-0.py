# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        preGroup = dummy

        while True:
            kth = self.getkth(preGroup,k)
            if kth is None: break
            nextGroup = kth.next

            prev = nextGroup
            cur = preGroup.next
            
            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = preGroup.next
            preGroup.next = kth
            preGroup = temp
        return dummy.next


    def getkth(self, node, k):
        kth = node
        while kth and k > 0:
            k -= 1
            kth = kth.next
        return kth 