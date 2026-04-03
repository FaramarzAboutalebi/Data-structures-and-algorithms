class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        minProd = 1
        maxProd = 1

        for n in nums:
            if n == 0:
                minProd = 1
                maxProd = 1
            temp = minProd
            minProd = min(minProd*n,maxProd*n,n)
            maxProd = max(temp*n,maxProd*n,n)
            res = max(res,maxProd)
        return res
            

        