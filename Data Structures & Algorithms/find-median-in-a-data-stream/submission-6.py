import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num) # O(log n)


        if self.minheap and self.minheap[0] < -self.maxheap[0]:
            n = heapq.heappop(self.maxheap) # O(log n)
            heapq.heappush(self.minheap, -n) # O(log n)        

        if len(self.minheap) > len(self.maxheap) + 1:
            n = heapq.heappop(self.minheap) # O(log n)
            heapq.heappush(self.maxheap, -n) # O(log n)
        if len(self.maxheap) > len(self.minheap) + 1:
            n = heapq.heappop(self.maxheap) # O(log n)
            heapq.heappush(self.minheap, -n) # O(log n)

        

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0] # O(1)
        elif len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0] #O(1)
        return (- self.maxheap[0] + self.minheap[0]) / 2.0
# for addNum() for n elements
# n current number of values stored in ds
# m number of method calls
# time complexity:  O(m logn)
# space complexity: O(n) 


# for addNum() for n elements
# time complexity:  O(m)
# space complexity: O(1)    