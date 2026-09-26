class Solution:
    def climbStairs(self, n: int) -> int:

        left,right = 1,1

        for i in range(n-1):
            left,right = left + right,left
        return left
        
# time complexity: O(n)
# space complexity: O(1)