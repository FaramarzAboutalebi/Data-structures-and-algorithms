class Solution:
    def climbStairs(self, n: int)->int:
        
        if n == 0:
            return 0
        left, right = 1, 1
        
        for _ in range(n-1):
            temp = left
            left = left + right
            right = temp
        return left
n = 1
print(Solution().climbStairs(n))
n = 3
print(Solution().climbStairs(n))