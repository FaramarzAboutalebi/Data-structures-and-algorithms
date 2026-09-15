"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        startList = [i.start for i in intervals]
        endList = [i.end for i in intervals]

        startList.sort()
        endList.sort()

        s,e = 0,0
        counter,res = 0,0

        while s < len(startList) and e < len(endList):
            if startList[s] < endList[e]:
                counter += 1
                s += 1
            else:
                counter -= 1
                e += 1
            res = max(counter,res)
        return res

# time complexity: O(n logn)
# space complexity(n)


        