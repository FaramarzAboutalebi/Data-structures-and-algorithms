"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hashMap = {}

        cur = head

        while cur != None:
            hashMap[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur != None:
            hashMap[cur].next = hashMap.get(cur.next)
            hashMap[cur].random = hashMap.get(cur.random)
            cur = cur.next

        return hashMap[head]




