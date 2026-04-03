class Solution:
    def climbStairs(self, n: int) -> int:
        right = 1
        left = 1
        
        for i in range(n-1):
            temp = left + right
            right = left
            left = temp
        return left
n = 5        
sol = Solution()
output = sol.climbStairs(n)
print(f"res = {output}")
            
            
        
        
        
        
        
        
        