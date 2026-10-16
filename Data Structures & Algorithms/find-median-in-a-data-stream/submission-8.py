import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [],[]   

    def addNum(self, num: int) -> None:
        # addNum for n
        # time complexity: O(n logn)
        # space complexity: O(n)
        
        if self.maxHeap and -self.maxHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -n)
        if len(self.minHeap) > len(self.maxHeap)+1:
            n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -n)
 

    def findMedian(self) -> float:
        # time complexity: O(1)
        # space complexity: O(1)
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        elif len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        
        