class Solution:
    def longestPalindrome(self, s: str)->str:
        if len(s) == 0:
            return ""
            
        res = [-1,-1]
        resLen = 0
        for i in range(len(s)):
            
            # odd
            l,r = i,i
            while(l >=0 and r < len(s) and s[l] == s[r]):
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = [l,r]
                l -= 1
                r += 1
                
            # even
            l,r = i,i+1
            while(l >=0 and r < len(s) and s[l] == s[r]):
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = [l,r]
                l -= 1
                r += 1
        l,r = res[0],res[1]
        return s[l:r+1]
        
# time complexity: O(n^2)
# space complexity: O(1)

s = "ababd"
print(Solution().longestPalindrome(s))
s = "abbc"
print(Solution().longestPalindrome(s))
