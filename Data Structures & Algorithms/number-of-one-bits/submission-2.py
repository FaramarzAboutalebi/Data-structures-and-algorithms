class Solution:
    def hammingWeight(self, number: int) -> int:
        counter = 0
        
        while number:
            if number & 1:
                counter += 1
            number >>= 1 # shift to right
        return counter
# time complexity: O(k), where k = number of bits in n (O(1) since k = 32)
# space complexity: O(1)
sol = Solution()
n = 5
print(sol.hammingWeight(n))