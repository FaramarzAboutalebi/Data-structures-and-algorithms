class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minProd, maxProd = 1,1
        res = max(nums)

        for num in nums:
            if num == 0:
                minProd, maxProd = 1,1
                continue
            temp = minProd
            minProd = min(num, num * minProd,num * maxProd)
            maxProd = max(num, num * temp,num * maxProd)
            res = max(res,maxProd)
        return res
        