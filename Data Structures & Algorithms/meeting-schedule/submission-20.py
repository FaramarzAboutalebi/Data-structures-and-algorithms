from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval])->bool:
        
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key = lambda i:i.start)
        
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True

# time complexity: O(n logn)
# space complexity: O(1)  

intervals = [Interval(0,2),Interval(1,5),Interval(6,10)]
sol = Solution()
print(sol.canAttendMeetings(intervals))