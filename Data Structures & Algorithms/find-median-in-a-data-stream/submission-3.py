import heapq

class MedianFinder:
    def __init__(self):
        self.maxHeap = [] # left
        self.minHeap = [] # right

    def addNum(self, num: int)->None:
        # time complexity: O(logn)
        if self.maxHeap and -self.maxHeap[0] < num:
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-num)
        
        if len(self.maxHeap) > len(self.minHeap)+1:
            n = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,n)
        if len(self.minHeap) > len(self.maxHeap)+1:
            n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -n)

    def findMedian(self)->float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        elif len(self.maxHeap) < len(self.minHeap):
            return float(self.minHeap[0])
        return (-self.maxHeap[0]+ self.minHeap[0]) / 2.0
# overal time complexity and space cplexity when we have n num:
# time complexity: O(n logn)
# space complexity: O(n) for heaps
med = MedianFinder()
#medianFinder.addNum(1);    // arr = [1]
med.addNum(1)
#medianFinder.findMedian(); // return 1.0
print(med.findMedian())
#medianFinder.addNum(3);    // arr = [1, 3]
med.addNum(3)
#medianFinder.findMedian(); // return 2.0
print(med.findMedian())
#medianFinder.addNum(2);    // arr[1, 2, 3]
med.addNum(2)
#medianFinder.findMedian(); // return 2.0
print(med.findMedian())
            
            