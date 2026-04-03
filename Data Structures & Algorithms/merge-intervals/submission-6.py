from typing import List

class Solution:
    def merge(self, intervals: List[List[int]])->List[List[int]]:
        
        if len(intervals) == 0:
            return []
            
        intervals.sort(key = lambda i:i[0]) # O(n logn)
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            start,end = intervals[i][0],intervals[i][1]
            if res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(intervals[i])
        return res
# time complexity: O(n logn)
# space complexity: O(k), k <= n
intervals = [[1,3],[1,5],[6,7]]
res = Solution().merge(intervals) == [[1,5],[6,7]]
print(res)

intervals = [[1,2],[2,3]]
res = Solution().merge(intervals) == [[1,3]]
print(res)
        