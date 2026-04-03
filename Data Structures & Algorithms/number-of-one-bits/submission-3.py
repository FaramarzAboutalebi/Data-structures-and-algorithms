class Solution:
    def hammingWeight(self, n: int)->int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count
# time complexity: O(32) -> O(1)
# space complexity: O(1)