class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):

            res += ((n & 1) << (31 - i))
            n >>= 1
        return res

# time complexity: O(32) or O(1)
# space complexity: O(1)

n = 1
sol = Solution()
print(sol.reverseBits(n) == (2 ** 31))