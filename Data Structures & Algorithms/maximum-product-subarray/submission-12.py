class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxP,minP = 1,1
        res = float("-inf")

        for n in nums:

            maxP,minP= max(n,maxP * n, minP * n),min(n,maxP * n, minP * n)

            res = max(res, maxP) 

            if n == 0:
                maxP,minP = 1,1

        return res
