from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution:
    def minMeetingRooms(self, intervals: List[Interval])->int:
        
        
        startList = [i.start for i in intervals]
        endList = [i.end for i in intervals]
        
        startList.sort()
        endList.sort()
        
        s, e = 0, 0
        res,counter = 0,0 

        while s < len(startList) and e < len(endList):
            
            if startList[s] < endList[e]:
                counter += 1
                s += 1
            else:
                e += 1
                counter -= 1
            res = max(res, counter)
        return res
                
            
        
        