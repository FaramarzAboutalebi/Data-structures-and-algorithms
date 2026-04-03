from typing import List

class Solution:
    def insert(self,intervals: List[List[int]], newInterval:List[int])->List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
        

        
sol = Solution()
intervals = [[1,3],[4,6]]
newInterval = [2,5]
Output = [[1,6]]
print(sol.insert(intervals,newInterval) == Output)

intervals = [[1,2],[3,5],[9,10]]
newInterval = [6,7]

Output = [[1,2],[3,5],[6,7],[9,10]]
print(sol.insert(intervals,newInterval) == Output)


# time complexity: O(n)
# space complexity: O(1)