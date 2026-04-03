class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        resLen = -1
        palindromNum = 0

        for i in range(len(s)):
            # odd
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                palindromNum += 1
                l -= 1
                r += 1
            # even
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                palindromNum += 1
                l -= 1
                r += 1
        return palindromNum