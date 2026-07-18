class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        largestFreq = 0
        res = 0
        counter = {}
        l = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r],0) + 1
            largestFreq = max(largestFreq,counter[s[r]])

            if (r-l+1) - largestFreq > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res,r-l+1)
        return res

# time complexity: O(n )
# space complexity: O(1)
