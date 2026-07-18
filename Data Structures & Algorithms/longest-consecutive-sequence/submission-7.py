class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        res = 0
        for n in numSet:

            if (n-1) not in numSet:
                lenght = 0
                while (n + lenght) in numSet:
                    lenght += 1
                res = max(res, lenght)
        return res

# time comeplxity: O(2n) = O(n)
# space complexity: O(n)