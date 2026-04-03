class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i:i[0])

        prevE = intervals[0][1]
        count = 0

        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]

            if start < prevE:
                count += 1
                prevE = min(prevE,end)
            else:
                prevE = end
        return count

# time complexity: O(n logn)
# space complexity: O(1)