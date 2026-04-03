class Solution:
    def getSum(self, a: int, b: int)->int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b:
            a, b = (a^b) & MASK, ((a&b) << 1) & MASK
        return a if a <= MAX_INT else ~(a ^ MASK)
# time complexity: O(32) -> O(1)
# space complexity: O(1)

sol = Solution()
a = 4
b = -7
print(sol.getSum(a,b))