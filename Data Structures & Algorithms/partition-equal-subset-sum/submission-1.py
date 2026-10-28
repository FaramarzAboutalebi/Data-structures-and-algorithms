class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total//2

        dp = {0}

        for num in nums:

            newDp = dp.copy()

            for s in dp:
                newDp.add(s+num)
            
            dp = newDp

            if target in dp:
                return True
        return False

# time complexity: O(n)
# space complexity: O(n) 