class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set()

        for n in nums:
            numSet.add(n)
        res = 0

        for n in nums:

            counter = 0
            checker = n
            while checker in numSet:
                counter += 1
                checker += 1
            res = max(res, counter)
        return res
            
# time     