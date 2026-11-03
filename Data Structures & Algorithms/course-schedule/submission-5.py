from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = defaultdict(list)

        for a,b in prerequisites:
            adj[a].append(b)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True
            visit.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            adj[course] = []
            visit.remove(course)
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
