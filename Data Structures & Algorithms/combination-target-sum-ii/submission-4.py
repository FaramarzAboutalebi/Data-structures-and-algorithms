class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res = []

        def dfs(stack,total,i):
            if target == total:
                res.append(stack.copy())
                return
            if i == len(candidates) or total > target:
                return

            
            stack.append(candidates[i])
            dfs(stack, total + candidates[i], i+1)

            stack.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(stack, total , i+1)
            

        dfs([],0,0)
        return res

# time complexity: O(n * 2^n + n logn) = O(n * 2^n)
# space complexity: O(n)