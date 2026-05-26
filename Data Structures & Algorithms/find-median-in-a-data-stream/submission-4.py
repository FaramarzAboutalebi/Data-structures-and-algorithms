import heapq

class MedianFinder:

    def __init__(self):

        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:


        heapq.heappush(self.maxHeap, -num)

        # make sure every maxHeap value <= every minHeap value
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if len(self.maxHeap)  > len(self.minHeap) + 1:
            n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, n * -1) # log n
        if len(self.maxHeap) + 1 < len(self.minHeap):
            n = heapq.heappop(self.minHeap) * (-1) 
            heapq.heappush(self.maxHeap, n)

        

    def findMedian(self) -> float:
        if len(self.maxHeap)  > len(self.minHeap):
            return (-1 * self.maxHeap[0])
        elif len(self.maxHeap)  < len(self.minHeap):
            return ( self.minHeap[0])
        else:
            return (-1 * self.maxHeap[0] + (self.minHeap[0]))/ 2.0
        
        