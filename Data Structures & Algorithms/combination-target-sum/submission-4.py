class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []

        def dfs(stack,total, i):
            if total == target:
                self.res.append(stack.copy())
                return
            if i >= len(nums) or total > target:
                return 
            
            stack.append(nums[i])
            dfs(stack,total+nums[i],i)

            stack.pop()
            dfs(stack,total,i+1)

            return


        dfs([],0, 0)
        return self.res

# time complexity: 2 ^ (N+ target/min(nums))
# space complexity: N + target/min(nums)
        