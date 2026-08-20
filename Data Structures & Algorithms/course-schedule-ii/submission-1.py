from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preReq = defaultdict(list)

        for course, prerequisite in prerequisites:
            preReq[course].append(prerequisite)
        
        visit = set()
        done = set()
        res = []

        def dfs(course):
            if course in visit:
                return False
            if course in done:
                return True

            visit.add(course)

            for prerequisite in preReq[course]:
                if not dfs(prerequisite):
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

# time complexity: O(E + V)
# space complexity: O(E + V)
        