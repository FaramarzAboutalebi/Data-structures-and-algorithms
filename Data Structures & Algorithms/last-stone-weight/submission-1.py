class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minHeap = []
        for w in stones:
            minHeap.append(-w)
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            w1 = -1 * heapq.heappop(minHeap)
            w2 = -1 * heapq.heappop(minHeap)

            if w1!=w2:
                heapq.heappush(minHeap, -1 * abs(w1-w2))
            
        return -1 * minHeap[0] if len(minHeap) else 0

        