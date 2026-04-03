class Solution:
    def reverseBits(self, n: int)->int:
        res = 0
        for i in range(32):
            num = (n >> i) & 1
            res += (num << (31-i))
        return res
        
# time complexity: O(32)
# space complexity: O(1)
sol = Solution()
print(sol.reverseBits(2818572288))