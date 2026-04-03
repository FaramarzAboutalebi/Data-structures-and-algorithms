from typing import List

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end
class Solution:
    def canAttendMeetings(self,intervals: List[Interval]):
        intervals.sort(key = lambda i : i.start)
        
        for i in range(1,len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
        
sol = Solution()
intervals = [Interval(0,30),Interval(5,10),Interval(15,20)]
print(sol.canAttendMeetings(intervals))

intervals = [Interval(5,8),Interval(9,15)]
print(sol.canAttendMeetings(intervals))

# time complexity: O(n logn)
# space complexity: O(1)