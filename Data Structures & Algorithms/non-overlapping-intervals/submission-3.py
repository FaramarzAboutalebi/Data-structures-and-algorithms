from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])->bool:
        
        intervals.sort(key = lambda i:i[0]) # O(n logn)
        
        prevEnd = intervals[0][1]
        count = 0 
        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]
            
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd,end)
        return count
# time complexity: O(n logn)
# space complexity: O(1)