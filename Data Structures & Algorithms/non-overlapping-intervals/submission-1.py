from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])->List[List[int]]:
        
        intervals.sort() # O(n logn)
        res = 0
        prevEnd = intervals[0][1]  
        
        for i in range(1,len(intervals)):
            if prevEnd <= intervals[i][0]: # no overlap
                prevEnd = intervals[i][1]
            else: #overlap
                res += 1
                prevEnd = min(prevEnd,intervals[i][1])
        return res
        
sol = Solution()
intervals = [[1,2],[2,4],[1,4]]
print(sol.eraseOverlapIntervals(intervals))
                
