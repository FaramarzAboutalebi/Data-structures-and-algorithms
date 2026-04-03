from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]])->bool:
        
        courseToPrereq = defaultdict(list)
        
        for course,preReq in prerequisites:
            courseToPrereq[course].append(preReq)
        visited = set()
        visiting = set()
        
        def dfs(i):
            if i in visited or courseToPrereq[i] == []:
                return True
            if i in visiting:
                return False
          
            visiting.add(i)

            for pre in courseToPrereq[i]:
                if not dfs(pre):
                    return False
            visited.add(i)
            visiting.remove(i)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
numCourses = 2
prerequisites = [[0,1],[1,0]]
print(Solution().canFinish(numCourses,prerequisites))
numCourses = 2
prerequisites = [[0,1]]
print(Solution().canFinish(numCourses,prerequisites))