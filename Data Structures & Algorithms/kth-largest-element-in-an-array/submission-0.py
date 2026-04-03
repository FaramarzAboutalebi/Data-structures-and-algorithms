class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minHeap = []
        for num in nums:

            minHeap.append(-1 * num)

        heapq.heapify(minHeap)
        res = 0
        while k:
            res = heapq.heappop(minHeap)
            k -= 1
        return res * -1
