from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for course,preReq in prerequisites:
            adj[course].append(preReq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True
            visit.add(course)

            for neiCourse in adj[course]:
                if not dfs(neiCourse):
                    return False

            visit.remove(course)
            adj[course] = []
            return True



        for n in range(numCourses):
            if not dfs(n):
                return False
        return True

# time complexity: O(E + V)
# space complexity: O(E + V)
        