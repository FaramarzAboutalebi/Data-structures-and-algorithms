class Solution:
    def getSum(self, a: int, b: int) -> int:

        MASK = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        return a if a < max_int else ~(a ^ MASK)


# time complexity: O(32) = O(1)
# space complexity: O(1)