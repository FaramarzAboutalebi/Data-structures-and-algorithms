from typing import List

class IntervalObj:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[IntervalObj])->int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        
        res = 0
        count = 0
        s,e = 0,0
        
        while s < len(start) and e < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
                
# time complexity: O(n logn)
# time complexity: O(n) for start and end
intervals = [IntervalObj(0,40),IntervalObj(5,10),IntervalObj(15,20)]
print(Solution().minMeetingRooms(intervals))


intervals = [IntervalObj(4,9)]
print(Solution().minMeetingRooms(intervals))