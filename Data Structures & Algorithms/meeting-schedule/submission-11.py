from typing import List

class IntervalObj:
    def __init__(self,start,end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[IntervalObj])->bool:
        
        if not intervals:
            return True
          
        intervals.sort(key = lambda i:i.start) 
        prevEnd = intervals[0].end
        
        for i in range(1,len(intervals)):
            start,end = intervals[i].start,intervals[i].end
            
            if start < prevEnd:
                return False
            prevEnd = end
        return True
      
# time complexity: O(n logn)
# space complexity: O(1)
intervals = [IntervalObj(0,30),IntervalObj(5,10),IntervalObj(15,20)]
print(Solution().canAttendMeetings(intervals)) 
intervals = [IntervalObj(5,8),IntervalObj(9,15)]
print(Solution().canAttendMeetings(intervals)) 

            
            
            
            
            