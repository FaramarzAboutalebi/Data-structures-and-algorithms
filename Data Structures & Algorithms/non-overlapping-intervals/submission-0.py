class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i:i[1])

        prevEnd = float("-inf")
        count = 0
        for start,end in intervals:

            if start < prevEnd:
                count += 1
            else:
                prevEnd = end
        return count