class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i][0],intervals[i][1]
            
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end  < newInterval[0]:
                res.append([start,end])
            else:
                newInterval[0], newInterval[1] = [min(start, newInterval[0]),max(end, newInterval[1])]
        res.append(newInterval)   
        return res

# time complexity: O(n)
# space complexity: O(n)