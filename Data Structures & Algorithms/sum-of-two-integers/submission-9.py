class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF # 111...111
        max_int = 0x7FFFFFFF # 011...111

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= max_int else ~(a ^ mask)

# time complexity: O(32) or O(1)
# space complexity: O(1)
        