from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])->int:
        if not intervals:
            return 0
        intervals.sort(key = lambda i:i[0])
        count = 0
        
        prevE = intervals[0][1]
        
        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]
            
            if prevE <= start:
                prevE = end
            else:
                prevE = min(prevE,end)
                count += 1
        return count
# time complexity: O(n logn)
# space complexity: O(1)      
sol = Solution()
intervals = [[1,2],[2,4],[1,4]]
print(sol.eraseOverlapIntervals(intervals))              
    