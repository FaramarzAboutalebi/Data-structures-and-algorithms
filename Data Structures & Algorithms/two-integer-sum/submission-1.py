class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numToIdx = {}

        for i in range(len(nums)):

            diff = target - nums[i] 
            
            if diff in numToIdx:
                return [numToIdx[diff], i]
            
            numToIdx[nums[i]] = i
        
        return []

# time complexity: O(n)
# space complextiy: O(n)