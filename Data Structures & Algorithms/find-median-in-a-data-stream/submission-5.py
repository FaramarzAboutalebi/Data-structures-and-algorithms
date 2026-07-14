import heapq
class MedianFinder:

    def __init__(self):

        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.maxheap, -num)

        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val) # log n

        if len(self.maxheap) > len(self.minheap) + 1:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)
        if len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-val)
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2.0





        
        