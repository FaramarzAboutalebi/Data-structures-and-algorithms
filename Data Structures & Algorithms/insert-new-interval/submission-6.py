from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval)->List[List[int]]:
        res = []
        for i in range(len(intervals)):
            
            start,end = intervals[i][0],intervals[i][1]
            
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append([start,end])
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        res.append(newInterval)
        return res
                