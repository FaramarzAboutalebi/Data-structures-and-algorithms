from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]):
        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            
            start,end = intervals[i][0],intervals[i][1]
            
            if res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(intervals[i]) # O(1)
        return res
intervals = [[1,3],[1,5],[6,7]]
print(Solution().merge(intervals))
# time complexity: O(n logn)
# space complexity: O(n)             