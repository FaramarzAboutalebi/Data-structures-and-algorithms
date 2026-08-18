class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preReq = defaultdict(list)

        for course, prerequisit in prerequisites:
            preReq[course].append(prerequisit)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preReq[course] == []:
                return True

            visit.add(course)

            for prerequisit in preReq[course]:
                if not dfs(prerequisit):
                    visit.remove(course)
                    return False
            
            visit.remove(course)
            preReq[course] = []
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

# time complexity: O(E + V)
# space complexity: O(E + V)
        