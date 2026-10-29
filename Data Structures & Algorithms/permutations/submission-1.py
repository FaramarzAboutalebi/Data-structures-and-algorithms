class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        stack = []
        visit = set()

        def dfs():

            if len(stack) == len(nums):
                res.append(stack.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] in visit:
                    continue
                
                stack.append(nums[i])
                visit.add(nums[i])

                dfs()

                stack.pop()
                visit.remove(nums[i])

        dfs()
        return res

# time complexity: O(n! * n)
# space complexity: O(n! * n)