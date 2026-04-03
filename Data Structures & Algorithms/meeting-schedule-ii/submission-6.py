from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval])->int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        s, e = 0, 0
        counter = 0
        res = 0
        
        while s < len(intervals) and e < len(intervals):
            if start[s] < end[e]:
                counter += 1
                s += 1
            else:
                counter -= 1
                e += 1
            
            res = max(res, counter)
  
        
        return res
        
# Time complexity: O(n log n)
# space complexity: O(n)

sol = Solution()
intervals = [Interval(0,20), Interval(1,5), Interval(5,7)]
print(sol.minMeetingRooms(intervals))
                