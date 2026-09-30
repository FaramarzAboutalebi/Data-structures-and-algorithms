class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}

        for course, preReq in prerequisites:
            adj[course].append(preReq)

        visit = set()
        
        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True

            visit.add(course)

            for preReq in adj[course]:
                if not dfs(preReq):
                    return False
            
            adj[course] = []
            visit.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

# time complexity:
