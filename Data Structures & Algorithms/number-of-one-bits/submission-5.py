class Solution:
    def hammingWeight(self, n: int)->int:
        res = 0
        while n:
            res += (n & 1)
            n >>= 1
        return res
        
# time complexity: O(32) -> O(1)
# space complexity: O(1)
sol = Solution()
print(sol.hammingWeight(3))