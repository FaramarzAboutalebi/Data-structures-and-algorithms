from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])->int:
        
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i[0])
        
        count = 0
        prevEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i][0],intervals[i][1]
            if prevEnd > start:
                count += 1
                prevEnd = min(prevEnd, end)
         
            else:
                prevEnd = end
        return count

                
            
            
            
            