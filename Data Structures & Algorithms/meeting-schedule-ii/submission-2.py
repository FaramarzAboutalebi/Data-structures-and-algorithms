"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:

from typing import List

class IntervalObj:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
class Solution:
    def minMeetingRooms(self, intervals: list[IntervalObj])->bool:
        
        intervals.sort(key = lambda i:i.start) # O(n logn)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        s, e = 0, 0
        count = 0
        res = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(count, res)
        return res
# time complexity: O(n logn)
# space complexity: O(n) for start and end                