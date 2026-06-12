class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set()

        for n in nums:
            numSet.add(n)
        res = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                res = max(res,length)

        return res
            
# time complexity: O(n)
# space complexity: O(n) 