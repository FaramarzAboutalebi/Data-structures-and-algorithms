class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0, n+1):

            # num
            # using shifting
            numofOnes = 0
            while num:
                numofOnes += (num & 1)
                num >>= 1
            res.append(numofOnes)
        return res

        