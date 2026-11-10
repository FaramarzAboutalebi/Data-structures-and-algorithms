class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list) # S: O(V+E)

        for course, preReq in prerequisites: # T: O(E)
            adj[course].append(preReq)

        visit = set()

        def dfs(course): # T: O(E + V)

            if course in visit:
                return False
            if adj[course] == []:
                return True


            visit.add(course)

            for preRes in adj[course]:
                if not dfs(preRes):
                    return False
            
            adj[course] = []
            visit.remove(course)
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

# time complexity: O(E + V)
# space complexity: O(E + V)
