from typing import List

class Solution:
    def merge(self, intervals: List[List[int]])->List[List[int]]:
        
        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            
            if res[-1][1] >= intervals[i][0]: #overlap
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
sol = Solution()
intervals = [[1,2],[2,3]]
print(sol.merge(intervals))