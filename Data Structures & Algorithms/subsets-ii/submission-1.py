class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
 
        res = []

        def dfs(i,stack):
            if i == len(nums):
                res.append(stack.copy())
                return
            
            stack.append(nums[i])
            dfs(i+1,stack)

            stack.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,stack)

        dfs(0,[])
        return res

# time complexity: O(n * 2^n)
# space complexity: O(n * 2^n)