from typing import List

class Solution:
    def merge(self, intervals: List[int])->List:
        
        if not intervals:
            return []
        
        intervals.sort(key = lambda i:i[0])
        res = []
        res.append([intervals[0][0],intervals[0][1]])
        
        for i in range(1, len(intervals)):
            satrt,end = intervals[i][0],intervals[i][1]
            if res[-1][1] < satrt:
                res.append([satrt,end])
            else:
                newEnd = max(end, res[-1][1])
                res[-1][1] = newEnd
        return res
intervals = [[1,3],[1,5],[6,7]]
print(Solution().merge(intervals))