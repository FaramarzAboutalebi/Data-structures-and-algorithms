class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) <= 1:
            return 0 

        intervals.sort(key = lambda i:i[0])
        
        prevEnd = intervals[0][1]
        counter = 0

        for i in range(1, len(intervals)):
            start,end = intervals[i][0],intervals[i][1]

            if start < prevEnd:
                counter += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return counter

# time complexity: O(n logn)
# space complexity: O(1)