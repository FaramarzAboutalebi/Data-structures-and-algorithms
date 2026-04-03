class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        return False

    def sumOfSquare(self,n):
        res = 0
        while n:
            digit = n % 10
            n = n//10
            res += (digit**2)
        return res
        