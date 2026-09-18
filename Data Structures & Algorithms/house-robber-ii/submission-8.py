class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0],self.robHelper(nums[:len(nums)-1]),self.robHelper(nums[1:]))
    
    def robHelper(self, nums):
        left,right = 0,0
        for n in nums:
            right, left = max(right, n + left),right
        return right

# time complexity: O(n)
# space compexity: O(1)           