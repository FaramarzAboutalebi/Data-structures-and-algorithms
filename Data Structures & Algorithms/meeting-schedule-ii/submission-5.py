from typing import List

class IntervalObj:
    def __init__(self, start,end):
        self.start = start
        self.end = end
class Solution:
    def minMeetingRooms(self, interval: List[IntervalObj])->int:
        
        start = sorted([i.start for i in interval])
        end = sorted([i.end for i in interval])
        
        s,e = 0,0
        res = 0
        counter = 0
        while s < len(interval) and e < len(interval):
            
            if start[s] < end[e]:
                counter += 1
                s += 1
            else:
                counter -= 1
                e += 1
            res = max(res, counter)
        return res
            
            
