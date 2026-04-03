class Solution:
    def reverse(self, x: int) -> int:

        MAX_INT = 2**31 -1
        sign = 1 if x >= 0 else -1
        x = abs(x)
        rev = 0

        while x:

            pop = x %10
            x //= 10

            if rev > MAX_INT // 10 or (rev == MAX_INT//10 and pop > 7):
                return 0

            rev = rev * 10 + pop
        rev *= sign
        return rev
        

        