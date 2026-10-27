class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        left,right = 0,0

        for i in range(len(cost)-1,-1,-1):
            left,right = cost[i] + min(left,right), left
        return min(left,right)


# time complexity: O(n)
# space complexity: O(1)