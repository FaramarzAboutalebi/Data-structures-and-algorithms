class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        

    def helper(self, subNums) -> int:
        one, two = 0,0

        for num in subNums:
            temp = max(num+one, two)
            one = two
            two = temp
        return two