class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = 0
        res_range = [-1,-1]

        for i in range(len(s)):

            #odd
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > res:
                    res = r-l+1
                    res_range = [l,r]
                l -= 1
                r += 1

            #even
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > res:
                    res = r-l+1
                    res_range = [l,r]
                l -= 1
                r += 1

        l,r = res_range[0],res_range[1]    
        return s[l:r+1]

# time complexity: O(n ^ 2)
# space complexity: O(1)