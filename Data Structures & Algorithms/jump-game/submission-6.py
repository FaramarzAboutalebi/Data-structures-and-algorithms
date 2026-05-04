class Solution:
    def canJump(self, nums)->bool:
        
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1,-1,-1):
            
            if nums[i] + i >= goal:
                goal = i
        return goal == 0

# time complexity: O(n)
# space complexity: O(1)
nums = [1,2,0,0,3]
sol = Solution()
print(sol.canJump(nums))