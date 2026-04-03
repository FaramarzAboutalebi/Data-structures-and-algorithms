class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()
        res = []

        hashmap = {i:[] for i in range(numCourses)}

        for cur,pre in prerequisites:
            hashmap[cur].append(pre)

        def dfs(cour):
            if cour in visited:
                return True
            if cour in visiting:
                return False
            visiting.add(cour)

            for pre in hashmap[cour]:
                if not dfs(pre): return False
            
            visiting.remove(cour)
            visited.add(cour)
            res.append(cour)
            return True
        for cours in range(numCourses):
            if not dfs(cours):
                return []
        return res        