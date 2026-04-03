class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashMap = {}
        maxFreq = 0
        maxLen = 0
        l = 0

        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, hashMap[s[r]])
            if (r-l+1) - maxFreq> k:
                hashMap[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen