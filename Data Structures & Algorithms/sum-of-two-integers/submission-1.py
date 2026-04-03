class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # Mask to get last 32 bits
        MAX_INT = 0x7FFFFFFF    # Max positive 32-bit int

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # If a is negative in 32-bit signed int, convert it
        return a if a <= MAX_INT else ~(a ^ MASK)
