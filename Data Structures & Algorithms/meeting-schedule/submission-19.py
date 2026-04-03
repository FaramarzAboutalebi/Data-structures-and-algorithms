from typing import List

class interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
class Solution:
    def canAttendMeetings(self, intervals: List[interval])->bool:
        
        intervals.sort(key = lambda x:x.start) # O(n log n)
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
        
# Time complexity: O(n log n)
# space complexity: O(1)

intervals = [interval(0,30), interval(5,10),interval(15,20)]
sol = Solution()
print(sol.canAttendMeetings(intervals))

intervals = [interval(5,8),interval(9,15)]
print(sol.canAttendMeetings(intervals))

