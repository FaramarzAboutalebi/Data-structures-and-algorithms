class Solution:
    def hammingWeight(self, number: int) -> int:
        counter = 0
        
        while number:
            if number & 1:
                counter += 1
            number >>= 1 # shift to right
        return counter
sol = Solution()
n = 5
print(sol.hammingWeight(n))