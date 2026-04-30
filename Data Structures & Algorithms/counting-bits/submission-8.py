class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n + 1)

        offSet = 1

        for i in range(1,n+1):

            if offSet * 2 == i:
                offSet = i
            dp[i] = dp[i-offSet] + 1 

        return dp

# Time complexity: O(n)
# space complexity: O(n)

        