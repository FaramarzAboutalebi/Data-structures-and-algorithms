class Solution:
    def getSum(self, a: int, b: int)->int:
        
        MASK = 0xFFFFFFFF
        MAX_INT = 0X7FFFFFFF
        
        while b != 0:
            a,b = (a^b) & MASK, ((a&b) << 1) & MASK
        
        return a if a <= MAX_INT else ~(a ^ MASK)
        
# time complexity: O(32) -> O(1)
# space complexity: O(1)
sol = Solution()
print(sol.getSum(2,3))