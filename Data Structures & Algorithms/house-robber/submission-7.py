class Solution:
    def rob(self, nums: List[int]) -> int:


        
        rob1,rob2 = 0,0

        for n in nums:

            rob2,rob1 = max(rob2,rob1+n),rob2
        return rob2

# time complexity: O(n)
# space complexity: O(1)