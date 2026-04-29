class Solution:
    def getSum(self, a: int, b: int)->int:
        
        max_int = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= max_int else ~(a ^ mask)
# time complexity: O(32) 0r O(1)
# space complexity: O(1)
a = 2
b = 6
sol = Solution()
print(sol.getSum(a,b))