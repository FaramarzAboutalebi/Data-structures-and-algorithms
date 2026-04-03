from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]):
        
        intervals.sort(key = lambda i:i[0]) # O(n logn)
        stack = [intervals[0]]
        
        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]
            if stack[-1][1] >= start: #overlapping
               stack[-1][1] = max(end, stack[-1][1]) 
            else:
                stack.append(intervals[i])
        return stack
intervals = [[1,3],[1,5],[6,7]]
print(Solution().merge(intervals))

# time complexity: O(n logn)
# space complexity: O(k)