class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        minP,maxP = 1,1
        for num in nums:
            if num == 0:
                minP,maxP = 1,1
                continue
            temp = maxP
            maxP = max(num, num * maxP,num * minP)
            minP = min(num, num * temp,num * minP)
            res = max(res, maxP)
        return res