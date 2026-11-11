from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        res = []
        adj = defaultdict(list)

        for course,preReq in prerequisites:
            adj[course].append(preReq)

        visit,done = set(),set()

        def dfs(course):

            if course in visit:
                return False
            if course in done:
                return True
            
            visit.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    visit.remove(course)
                    return False
            
            visit.remove(course)
            done.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res

# time complexity: O(V + E)
# space complexity: O(V + E)
        