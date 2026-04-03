class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = {}

        for n in hand:
            count[n] = count.get(n,0) + 1
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        # 1,2,3
        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in count: return False
                count[i] -= 1
                if count[i] == 0:
                    if minHeap[0] != i: return False
                    heapq.heappop(minHeap)
        return True