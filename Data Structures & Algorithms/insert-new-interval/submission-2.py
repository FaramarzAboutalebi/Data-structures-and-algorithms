from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval:List[int])-> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start,end = intervals[i]
            
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append(intervals[i])
            else:
                newInterval = [min(start,newInterval[0]),max(end,newInterval[1])]
        res.append(newInterval)
        return res
        
sol = Solution()
intervals = [[1,3],[4,6]]
newInterval = [2,5]
print(sol.insert(intervals,newInterval))
                
                
    