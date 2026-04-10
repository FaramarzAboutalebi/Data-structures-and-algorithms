class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        l = 0
        counter = {}

        for r in range(len(s)):

            counter[s[r]] = counter.get(s[r],0) + 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res


# time complexity: O(n)
# space complexity: O(1) 