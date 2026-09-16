class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxP,minP = 1,1
        res = max(nums)
        for n in nums:
            if n == 0:
                maxP,minP = 1,1
                continue
            temp = maxP
            maxP = max(n, maxP*n, minP*n)
            minP = min(n, temp*n, minP*n)
            res = max(res, maxP)

        return res
        

# time complexity: O(n)
# space complexity: O(1)