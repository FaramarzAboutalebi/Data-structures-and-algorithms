from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        for a,b in prerequisites:
            adj[a].append(b)

        res = []
        visit = set()
        done = set()
        
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

            done.add(course)
            visit.remove(course)
            res.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []
        return res

# time complexity: O(V + E)
# space complexity: O(V + E)
        