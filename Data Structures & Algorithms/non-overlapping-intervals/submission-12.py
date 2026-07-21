class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0


        intervals.sort(key = lambda x:x[0])
        res = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            s,e = intervals[i][0],intervals[i][1]

            if s < prevEnd:
                res += 1
                prevEnd = min(prevEnd, e)
            else:
                prevEnd = e
        return res

# time complexity: O(n log n)
# space complexity: O(1)