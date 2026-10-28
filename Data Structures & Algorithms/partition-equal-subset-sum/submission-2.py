from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            nextDp = dp.copy()

            for s in dp:
                nextDp.add(s + num)

            dp = nextDp

            if target in dp:
                return True

        return False

# Time complexity: O(n * target)
# Space complexity: O(target)