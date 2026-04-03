class Solution:
    def climbStairs(self, n: int)->int:
        point1 = 1
        point2 = 1
        
        for i in range(n-1):
            temp = point1
            point1 = point1 + point2
            point2 = temp
        return point1

# time complexity: O(n)
# space complexity: O(1)
sol = Solution()
n = 3
print(sol.climbStairs(n))