# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # N node and k lists
        # time complexity: O(N log k)
        # space complexity: O(k) for level


        while len(lists) > 1:
            level = []
            for i in range(0,len(lists),2):

                l1 = lists[i] 
                l2 = lists[i+1] if i+1 < len(lists) else None

                newLinkedList = self.margeTwoLinkedList(l1,l2)
                level.append(newLinkedList)
            if level:
                lists = level

        return lists[0] if lists else None



    def margeTwoLinkedList(self, h1,h2)->Optional[ListNode]:
        # time complexity: O(n1 + n2)
        # space complexity: O(1)
        dummy = ListNode()
        temp = dummy

        while h1 and h2:

            if h1.val < h2.val:
                temp.next = h1
                h1 = h1.next
            else:
                temp.next = h2
                h2 = h2.next
            temp = temp.next

        if h1:
            temp.next = h1
        if h2:
            temp.next = h2
        
        return dummy.next