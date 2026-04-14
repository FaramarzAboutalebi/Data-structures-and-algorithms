class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = {}
        maxLen = 0
        maxFreq = 0
        l = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxFreq = max(maxFreq, counter[s[r]])

            if (r-l+1) - maxFreq > k:
                counter[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
        
        return maxLen


# time complexity: O(n)
# space complexity: O(1)