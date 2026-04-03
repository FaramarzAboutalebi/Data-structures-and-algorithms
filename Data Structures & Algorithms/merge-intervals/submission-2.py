from typing import List

class Solution:
    def merge(self, intervals: List[List[int]])-> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda i:i[0]) # n log n
        
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]
            
            if res[-1][1] >= start: #overlap
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(intervals[i])
        return res
                
        
        
sol = Solution()
intervals = [[1,2],[2,4],[1,4]]
print(sol.merge(intervals))              
    